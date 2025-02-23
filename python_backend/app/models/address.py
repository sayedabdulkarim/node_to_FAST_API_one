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
    type: str = Field(..., regex='^(Home|Work|Other)$')  # Match Node.js enum

class AddressModel(AddressCreate):
    user: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
