# 🧠 Person Detection with YOLOv8 & MQTT
This project demonstrates real-time person detection using YOLOv8, OpenCV, and MQTT.

It consists of two scripts:

Publisher → Detects persons in video frames and publishes images to an MQTT broker.
Subscriber → Receives the images and saves them to disk automatically.
✨ Features

✔ Real-time person detection using YOLOv8
✔ Publishes detected frames over MQTT
✔ Subscriber saves received images with timestamped filenames
✔ Auto-run subscriber on reboot using systemd
✔ Organized directory for saved images

# 🖥 Hardware Requirements
Any Linux device (tested on Yocto build system)
Camera (USB or CSI) for video capture
MQTT Broker (e.g., Mosquitto running on LAN)

# 📦 Software Requirements
Python 3.8+
Virtual Environment (venv) recommended
Libraries:
ultralytics
opencv-python
paho-mqtt




Enable the service:

sudo systemctl daemon-reload
sudo systemctl enable project1.service
sudo systemctl start project1.service
