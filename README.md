# 🐾 CatFeeder Watchdog

An AI-powered feeding session logger and dashboard for your cat, built with Raspberry Pi, OpenCV, and Streamlit.

This project automatically logs when your cat visits the feeding area, captures a photo, and displays stats and trends on a live dashboard.

---

## 📸 Features

- 📷 Automatic snapshot capture using Raspberry Pi camera or USB webcam
- ⏱️ Logs feeding duration and timestamps to `sessions.csv`
- 📊 Real-time dashboard with:
  - Total sessions and average durations
  - Time-of-day trends
  - Duration category distribution
  - Live snapshot gallery
- 🧠 Built with OpenCV, Streamlit, Plotly, and Python 3
- 🐍 Lightweight and designed for Raspberry Pi

---

## 🚀 Getting Started

1. Flash Raspberry Pi OS (Bookworm)
Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and enable SSH + Wi-Fi in advanced settings.

2. Install Git (if not installed)

sudo apt update
sudo apt install git

3. Clone this repository

cd ~
git clone https://github.com/rafiky1/catfeederwatch.git
cd catfeederwatch


4. Set up your environment

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

If you don’t have a requirements.txt, install manually:

pip install streamlit pandas plotly opencv-python-headless pillow

📂 Project Structure

catfeederwatch/
├── cat_logger.py         # Logs feeding events + captures snapshots
├── dashboard.py          # Streamlit dashboard
├── snapshots/            # Captured images
├── sessions.csv          # Feeding logs
├── start_feeder.sh       # Startup script (optional)
└── README.md

🧪 Run It

Start the API Server
uvicorn api_server:app --host 0.0.0.0 --port 8000

Start the Logger
python3 cat_logger.py

Start the Dashboard
streamlit run dashboard.py

(Optional) Enable Auto Start on Boot

chmod +x start_feeder.sh

To run: ./start_feeder.sh

sudo systemctl enable catfeeder.service
sudo systemctl start catfeeder.service

to check if it's running: 
sudo systemctl status catfeeder.service

📸 Screenshots

<img width="1205" alt="Screenshot 2025-05-06 at 8 27 52 PM" src="https://github.com/user-attachments/assets/b70ac53d-d88c-4efa-9e52-914c67393bf3" />
<img width="1226" alt="Screenshot 2025-05-06 at 8 27 59 PM" src="https://github.com/user-attachments/assets/7a3f72e9-3232-4575-8c4c-a6ee5bb076ff" />
<img width="1232" alt="Screenshot 2025-05-06 at 8 28 05 PM" src="https://github.com/user-attachments/assets/9adc6ee2-d4ae-431d-934a-fa5b2b752de8" />
<img width="1217" alt="Screenshot 2025-05-06 at 8 28 17 PM" src="https://github.com/user-attachments/assets/02488091-2c87-4bc7-af63-77d19a73b57c" />
<img width="1250" alt="Screenshot 2025-05-06 at 8 28 23 PM" src="https://github.com/user-attachments/assets/59287e88-f9cc-4e85-9129-34b332a3cf5e" />
<img width="1205" alt="Screenshot 2025-05-06 at 8 28 30 PM" src="https://github.com/user-attachments/assets/02b47c9f-d5de-45f1-b408-20fd445be307" />
<img width="1191" alt="Screenshot 2025-05-06 at 8 28 38 PM" src="https://github.com/user-attachments/assets/3673f32f-d9e0-4fbd-93ee-42b409bf6113" />





