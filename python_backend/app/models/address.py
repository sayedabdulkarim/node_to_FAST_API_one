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
    doorNumber: Optional[str] = None
    landmark: Optional[str] = None
    location: Location
    type: str = Field(..., pattern="^(Home|Work|Other)$")

class AddressModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    user: PyObjectId
    address: str
    doorNumber: Optional[str] = None
    landmark: Optional[str] = None
    location: Location
    type: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True
        populate_by_name = True
