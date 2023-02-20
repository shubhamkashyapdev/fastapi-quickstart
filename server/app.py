from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from server.db.db import get_db
from sqlalchemy.orm import Session
from server.sockets.socket import io
from server.schemas.device_schema import Device
from server.models.device_model import DeviceModel
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"])


@app.get('/health-check')
async def health_check(db: Session = Depends(get_db)):
    return 'API is working fine!'

@app.get('/device')
async def get_all_device(db: Session = Depends(get_db)):
    return db.query()

@app.post('/device')
async def create_device(db: Session = Depends(get_db), input = Device):
    device = DeviceModel(
        is_device_on=True,
        device_count=100
    )
    db.add(device)
    db.commit()
    db.refresh(device)
    print(device.device_count)
    # device = DeviceModel(is_device_on=input.is_device_on, device_count=input.device_count)
    # print(device)
    # db.add(device)
    # db.commit()
    # db.refresh(device)
    return 'trying to make it work'



app.mount('/ws', app=io)