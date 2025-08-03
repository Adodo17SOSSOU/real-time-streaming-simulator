import asyncio
import json
import websockets
import sys
import os

sys.path.append(os.path.dirname(__file__))  # Ensure local imports work
from data_generator import generate_sensor_data, append_to_csv

async def stream_data(websocket):
    print(f"Client connected: {websocket.remote_address}")
    try:
        while True:
            data = generate_sensor_data()
            append_to_csv(data)
            await websocket.send(json.dumps(data))
            await asyncio.sleep(1)
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected: {websocket.remote_address}")

async def main():
    async with websockets.serve(stream_data, "localhost", 8765):
        print("WebSocket server started at ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())

