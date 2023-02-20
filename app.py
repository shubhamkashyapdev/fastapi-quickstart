from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sockets.socket import io
from schemas.device_schema import Device
from models.device_model import DeviceModel

from db.db import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"])


@app.get('/health-check')
async def health_check(db: Session = Depends(get_db)):
    return 'API is working fine!'

@app.get('/device')
async def get_all_device(db: Session = Depends(get_db)):
    return db.query(DeviceModel).all()

@app.post('/device')
async def create_device(input: Device, db: Session = Depends(get_db)):
    device = DeviceModel(
        is_device_on=True,
        device_count=100
    )
    db.add(device)
    db.commit()
    db.refresh(device)
    return device



app.mount('/ws', app=io)