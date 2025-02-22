from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId

class Location(BaseModel):
    type: str = "Point"
    coordinates: List[float]

class AddressCreate(BaseModel):
    address: str
    doorNumber: str
    landmark: Optional[str] = None
    location: Location
    type: str

class AddressModel(AddressCreate):
    user: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
