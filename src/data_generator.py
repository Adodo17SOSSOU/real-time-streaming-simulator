import numpy as np
import pandas as pd
from datetime import datetime
import os

def generate_sensor_data():
    """
    Generate a single row of fake multivariate time series data.
    Returns a dict with timestamp and 4 sensor values.
    """
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu": round(np.random.uniform(20, 80), 2),       # % CPU usage
        "mem": round(np.random.uniform(30, 90), 2),       # % Memory usage
        "disk_io": round(np.random.uniform(50, 200), 2),  # MB/s
        "net": round(np.random.uniform(10, 100), 2)       # KB/s
    }

def append_to_csv(data, file_path="data/stream_log.csv"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df = pd.DataFrame([data])
    # Append to CSV, add header if file does not exist
    df.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False)

