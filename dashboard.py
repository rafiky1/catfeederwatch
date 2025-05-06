import streamlit as st
import pandas as pd
from datetime import datetime
import os
import plotly.express as px

# ---- Config ----
CSV_FILE = "sessions.csv"
LIVE_IMAGE_PATH = "latest.jpg"
MIN_DURATION = 15
ALERT_THRESHOLD_MIN = 360  # 6 hours

# ---- Page Setup ----
st.set_page_config(page_title="CatFeeder Watchdog", layout="wide")
st.title("🐾 CatFeeder Watchdog Dashboard")

# ---- Load and Filter Data ----
if not os.path.exists(CSV_FILE):
    st.info("No feeding session data available yet.")
    st.stop()

df = pd.read_csv(CSV_FILE, names=["timestamp", "duration", "image"])
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["duration"] = pd.to_numeric(df["duration"], errors="coerce")
df = df.dropna()
df = df[df["duration"] >= MIN_DURATION]

# ---- Download Button ----
csv_data = df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download Feeding Log (CSV)", data=csv_data, file_name="sessions.csv", mime="text/csv")

# ---- Summary Stats ----
st.markdown("### 📊 Feeding Summary Stats")
col1, col2, col3 = st.columns(3)

col1.metric("Total Sessions", len(df))
col2.metric("Average Duration", f"{df['duration'].mean():.1f}s")
col3.metric("Last Duration", f"{df['duration'].iloc[-1]:.1f}s")

# ---- Time Since Last Feeding ----
last_time = df["timestamp"].iloc[-1]
minutes_since = (datetime.now() - last_time).total_seconds() / 60
st.success(f"✅ Last feeding was {int(minutes_since)} minutes ago.")
if minutes_since > ALERT_THRESHOLD_MIN:
    st.warning("⚠️ Alert: No feeding detected in the last 6 hours!")

st.markdown("---")

# ---- Feeding by Hour (Plotly) ----
st.markdown("### ⏰ Feeding Pattern by Hour")

df["hour"] = df["timestamp"].dt.hour
hourly = df["hour"].value_counts().sort_index().reset_index()
hourly.columns = ["Hour", "Count"]

# 🌟 Peak feeding hour
peak_hour = df["hour"].mode()[0]
peak_count = df["hour"].value_counts().loc[peak_hour]
st.info(f"🌟 Peak feeding time: **{peak_hour}:00** with **{peak_count} sessions**")

# Plot
fig1 = px.bar(hourly, x="Hour", y="Count", title="Sessions by Hour", labels={"Count": "Number of Sessions"})
st.plotly_chart(fig1, use_container_width=True)

# ---- Daily Feeding Trend (Toggle Between Average vs Total) ----
st.markdown("### 📈 Feeding Duration Trend Over Time")

# Floor timestamps to clean daily labels
df["day"] = df["timestamp"].dt.floor("D")

# Dropdown to choose chart type
chart_type = st.selectbox("Choose chart type:", ["Average Duration per Day", "Total Feeding Time per Day"])

if chart_type == "Average Duration per Day":
    daily_avg = df.groupby("day")["duration"].mean().reset_index()

    fig = px.line(
        daily_avg,
        x="day",
        y="duration",
        title="Average Feeding Duration per Day",
        labels={"day": "Date", "duration": "Average Duration (s)"},
        markers=True
    )
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_tickformat="%b %d", xaxis_title=None)

else:
    daily_total = df.groupby("day")["duration"].sum().reset_index()

    fig = px.bar(
        daily_total,
        x="day",
        y="duration",
        title="Total Feeding Time per Day",
        labels={"day": "Date", "duration": "Total Duration (s)"},
        text_auto=True
    )
    fig.update_layout(xaxis_tickformat="%b %d", xaxis_title=None)

# Display chart
st.plotly_chart(fig, use_container_width=True)

# ---- Duration Histogram ----
st.markdown("### 📊 Feeding Session Duration Histogram")
fig3 = px.histogram(df, x="duration", nbins=20, title="Distribution of Feeding Durations", labels={"duration": "Seconds"})
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# ---- Recent Snapshots ----
st.markdown("### 📷 Recent Feeding Snapshots")
recent = df.tail(3)
img_cols = st.columns(3)
for i, (_, row) in enumerate(recent.iterrows()):
    with img_cols[i]:
        st.image(row["image"], caption=f"{row['timestamp']}  \n{row['duration']:.1f}s", use_column_width=True)

st.markdown("---")

# ---- Live Snapshot ----
st.markdown("### 📡 Live Camera Snapshot")
if os.path.exists(LIVE_IMAGE_PATH):
    st.image(LIVE_IMAGE_PATH, caption="Live View (updated every few seconds)", use_column_width=True)
    if st.button("🔄 Refresh Live Image"):
        st.experimental_rerun()
else:
    st.info("Live image not available yet. Make sure `latest.jpg` is being updated.")
