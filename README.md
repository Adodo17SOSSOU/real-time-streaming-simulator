# Project 1: Real-Time Streaming Simulator

This project simulates **real-time multivariate sensor data** and streams it to clients using **WebSockets**.
It also **logs all data to CSV** for later analysis.

This is **Project 1** of a 5-project series designed to **master real-time data streaming, anomaly detection, and visualization**.

---

## 📌 Features

* **Multivariate sensor simulation**:

  * CPU usage (%)
  * Memory usage (%)
  * Disk I/O (MB/s)
  * Network traffic (KB/s)
* **Real-time WebSocket streaming**
* **Automatic CSV logging**
* **Test client to receive data**
* **Lightweight & cross-platform**

---

## 📂 Project Structure

```
project1_stream_simulator/
│
├── data/                       # Logged CSV data
├── src/
│   ├── data_generator.py        # Generates sensor data
│   ├── stream_server.py         # WebSocket server
│   └── test_client.py           # Simple client to receive data
│
├── requirements.txt             # Python dependencies
└── README.md
```

---

## ⚡ Quick Start

### 1️⃣ Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install --upgrade pip
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start the WebSocket Server

```bash
python src/stream_server.py
```

Output:

```
WebSocket server started at ws://localhost:8765
```

---

### 4️⃣ Connect a Client

In a **new terminal**:

```bash
python src/test_client.py
```

Example output:

```
Connected to server. Listening for data...
Received: {"timestamp":"2025-08-03 14:00:00","cpu":47.2,"mem":62.1,"disk_io":120.0,"net":58.0}
Received: {"timestamp":"2025-08-03 14:00:01","cpu":49.1,"mem":61.9,"disk_io":118.0,"net":65.0}
```

---

### 5️⃣ Check the CSV Log

All generated data is saved to:

```
data/stream_log.csv
```

Example:

```
timestamp,cpu,mem,disk_io,net
2025-08-03 14:00:00,47.2,62.1,120.0,58.0
2025-08-03 14:00:01,49.1,61.9,118.0,65.0
```

---

## 🛠 Tech Stack

* **Python 3.10+**
* **WebSockets (`websockets` library)**
* **NumPy & Pandas** for data simulation and CSV handling

---

## 🚀 Next Steps

This simulator will serve as the **data source** for upcoming projects:

1. **Real-Time Anomaly Detection**
2. **Live Data Visualization Dashboard**
3. **ML-Based Predictive Analytics**
4. **Cloud Deployment with Kafka/MQTT**

---



