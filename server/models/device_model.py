from sqlalchemy import Boolean, Column, Integer 
from server.db.db import Base 

class DeviceModel(Base):
    __tablename__ = 'device'
    
    id = Column(Integer, primary_key=True, index=True)
    is_device_on = Column(Boolean)
    device_count = Column(Integer)