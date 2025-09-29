from paho.mqtt import client as mqtt_client
from datetime import datetime
import os

broker = '192.168.8.186'
port = 1883
topic = "photos"
client_id = 'sub_xzcfghjt123'  # different from publisher

# Directory to save images
save_dir = "/home/yocto/Desktop/mqtt/subscriber/Received_pictures"
os.makedirs(save_dir, exist_ok=True)  # create folder if not exists

# Counter for images
image_counter = 1

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("-------------------------Connected to MQTT broker-------------------------")
        else:
            print(f"-------------------------Failed to connect, return code {rc}-------------------------")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global image_counter
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        filename = f"image_{image_counter}_{timestamp}.jpeg"
        filepath = os.path.join(save_dir, filename)

        # Save image
        with open(filepath, 'wb') as f:
            f.write(msg.payload)

        print(f"-------------------------Person Detected-------------------------\nImage saved at: {filepath}")
        image_counter += 1

    client.subscribe(topic)
    client.on_message = on_message


def main():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    main()
