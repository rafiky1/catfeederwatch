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
  - Live snapshot gallery with "View All" toggle
- 🧠 Built with OpenCV, Streamlit, Plotly, and Python 3
- 🐍 Lightweight and designed for Raspberry Pi

---

## 🚀 Getting Started

### 1. Flash Raspberry Pi OS (Bookworm)
Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and enable SSH + Wi-Fi in advanced settings.

2. Clone this repository

'''bash
git clone https://github.com/rafiky1/catfeederwatch.git
cd catfeederwatch

3. Set up your environment

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

Pass a duration (in seconds) to simulate a feeding event.

Start the Dashboard

streamlit run dashboard.py

(Optional) start_feeder.sh (Auto startup script)

chmod +x start_feeder.sh

To run: ./start_feeder.sh


✅ Add and Push to GitHub

📸 Screenshots



