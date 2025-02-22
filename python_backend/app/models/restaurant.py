from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from .user import PyObjectId

class ImageBadge(BaseModel):
    imageId: str
    description: str

class TextExtendedBadge(BaseModel):
    iconId: str
    shortDescription: str
    fontColor: str

class Badges(BaseModel):
    imageBadges: List[ImageBadge] = []
    textExtendedBadges: List[TextExtendedBadge] = []

class SLA(BaseModel):
    deliveryTime: int
    lastMileTravel: float
    serviceability: str
    slaString: str
    lastMileTravelString: str
    iconType: str

class Availability(BaseModel):
    startTime: str
    nextCloseTime: str
    opened: bool

class AggregatedDiscountInfoV3(BaseModel):
    header: str
    subHeader: str
    discountTag: str

class RestaurantModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    aggregatedDiscountInfoV3: Optional[AggregatedDiscountInfoV3]
    areaName: str
    availability: Availability
    avgRating: float
    avgRatingString: str
    badges: bool
    cloudinaryImageId: str
    costForTwo: str
    cuisines: List[str]
    isOpen: bool
    name: str
    sla: SLA
    totalRatingsString: str
    type: str
    veg: bool
    adminUserId: PyObjectId
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True
        populate_by_name = True

class RestaurantCreate(BaseModel):
    name: str
    areaName: str
    avgRating: float
    cloudinaryImageId: str
    costForTwo: str
    cuisines: List[str]
    isOpen: bool = True
    veg: bool
    availability: Availability
    sla: SLA

class RestaurantUpdate(BaseModel):
    name: Optional[str]
    areaName: Optional[str]
    avgRating: Optional[float]
    isOpen: Optional[bool]
    costForTwo: Optional[str]
    cuisines: Optional[List[str]]
    veg: Optional[bool]

class RestaurantResponse(BaseModel):
    id: str
    name: str
    areaName: str
    avgRating: float
    cloudinaryImageId: str
    costForTwo: str
    cuisines: List[str]
    isOpen: bool
    veg: bool
