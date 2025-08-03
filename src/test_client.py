import asyncio
import websockets

async def receive_data():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to server. Listening for data...")
        while True:
            data = await websocket.recv()
            print("Received:", data)

if __name__ == "__main__":
    asyncio.run(receive_data())

