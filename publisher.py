from ultralytics import YOLO
import cv2
import time
from paho.mqtt import client as mqtt_client

# MQTT config
broker = '192.168.8.186'
port = 1883
topic = "photos"
client_id = 'pub_xzcfghjt123'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print(f"Failed to connect, return code {rc}")

    client = mqtt_client.Client(client_id=client_id, protocol=mqtt_client.MQTTv311)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish_image(client, image_bytes):
    result = client.publish(topic, image_bytes, qos=2)
    if result[0] == 0:
        print("Image sent!")
    else:
        print("Failed to send image")

# Load YOLO model
model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)
client = connect_mqtt()
client.loop_start()

frame_id = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    # Check if person is detected
    person_detected = any((r.boxes.cls == 0).any() for r in results)
    if person_detected:
        annotated_frame = results[0].plot()  # draw boxes on first result
        # Encode as JPEG bytes
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        image_bytes = buffer.tobytes()
        publish_image(client, image_bytes)
        frame_id += 1
        print(f"Person detected, frame {frame_id} sent")

    # Small delay to avoid flooding broker
    time.sleep(0.5)

cap.release()
client.loop_stop()
