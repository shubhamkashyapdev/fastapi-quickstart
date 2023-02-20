from pydantic import BaseModel, Field

class Device(BaseModel):
    is_device_on: bool = Field(title='Device Status')
    device_count: int