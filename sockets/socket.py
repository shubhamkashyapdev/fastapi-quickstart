import socketio 

server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

io = socketio.ASGIApp(
    socketio_server=server
)

@server.event
async def connect(sid, environ, auth):
    print(f"client connected {sid}")