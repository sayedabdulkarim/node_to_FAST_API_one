from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId
from .address import Location

class CartItem(BaseModel):
    name: str
    description: Optional[str] = None
    imageId: Optional[str] = None
    inStock: Optional[bool] = True
    price: float
    variants: Optional[List[dict]] = []
    offers: Optional[List[dict]] = []
    count: int = Field(ge=1)

class AddressDetails(BaseModel):
    address: str
    doorNumber: str
    landmark: Optional[str] = None
    location: Location
    type: str = Field(..., regex='^(Home|Work|Other)$')

class CartCreate(BaseModel):
    restaurantId: str
    addressDetails: AddressDetails
    items: List[CartItem]
    finalCost: float

class CartModel(CartCreate):
    userId: PyObjectId
    status: str = Field(default="active", regex='^(active|accept|completed|reject|pending)$')
    cancelledReason: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
