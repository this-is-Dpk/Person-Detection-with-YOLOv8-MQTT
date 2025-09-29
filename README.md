# 🧠 Person Detection with YOLOv8 & MQTT
# stm32-smart-weather-rtos
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

🖥 Hardware Requirements
Any Linux device (tested on Yocto build system)
Camera (USB or CSI) for video capture
MQTT Broker (e.g., Mosquitto running on LAN)
📦 Software Requirements
Python 3.8+
Virtual Environment (venv) recommended
Libraries:
ultralytics
opencv-python
paho-mqtt
📂 Project Structure
mqtt_person_detection/
├── publisher.py        # YOLOv8 + MQTT Publisher
├── subscriber.py       # MQTT Subscriber
├── requirements.txt    # Dependencies
├── Makefile            # Build & Run helper
└── README.md           # Documentation

⚙️ Installation & Setup
1️⃣ Clone this repository
git clone https://github.com/yourusername/mqtt_person_detection.git
cd mqtt_person_detection

2️⃣ Create and activate virtual environment
python3 -m venv yocto_venv
source yocto_venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

🚀 Usage
▶ Run Publisher

Detects persons from camera feed and publishes images:

make run-pub

▶ Run Subscriber

Receives and saves images into:

/home/yocto/Desktop/mqtt/subscriber/Received_pictures

make run-sub

🔄 Auto Start Subscriber on Boot

Create a systemd service file:
/etc/systemd/system/project1.service

[Unit]
Description=MQTT Subscriber Auto Start
After=network.target

[Service]
User=root
WorkingDirectory=/home/root
ExecStart=/bin/bash -c 'source /home/root/yocto_venv/bin/activate && python3 /home/root/project1.py'
Restart=always

[Install]
WantedBy=multi-user.target


Enable the service:

sudo systemctl daemon-reload
sudo systemctl enable project1.service
sudo systemctl start project1.service
