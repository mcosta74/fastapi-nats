import asyncio

from fastapi import FastAPI
from nats.aio.client import Client as NATS

from .models import UppercaseRequest, UppercaseResponse
from .service import main_service

app = FastAPI()
nats = NATS()

@app.get('/')
async def index():
    return {'results': 'Hello World'}


@app.post('/uppercase', response_model=UppercaseResponse)
async def uppercase(body: UppercaseRequest):
    resp = UppercaseResponse(results=main_service.uppercase(body.message))
    return resp


async def consume(loop: asyncio.AbstractEventLoop):
    async def message_handler(msg):
        print('New Message:', msg.subject, msg.reply, msg.data.decode())
        output = main_service.uppercase(msg.data.decode())

        if msg.reply:
            await nats.publish(msg.reply, output.encode())

    global nats

    print('Connecting to NATS....')
    await nats.connect(loop=loop)
    print('Connected')

    await nats.subscribe('cmd.uppercase', cb=message_handler)

    while True:
        await asyncio.sleep(1, loop=loop)


@app.on_event('startup')
async def connect_to_nats():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(consume(loop))
    print('INIT DONE')

@app.on_event('shutdown')
async def disconnect_to_nats():
    print('bye')