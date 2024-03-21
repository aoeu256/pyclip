import asyncio
import websockets
import ast

async def websocket_server(websocket, path):
    while True:
        message = await websocket.recv()
        print("Message from client:", message)
        
        try:
            result = eval(message)
            await websocket.send(str(result))
        except Exception as e:
            await websocket.send("Error: " + str(e))

start_server = websockets.serve(websocket_server, 'localhost', 5000)

asyncio.get_event_loop().run_until_complete(start_server)
print("Server running at ws://localhost:5000/")
asyncio.get_event_loop().run_forever()
