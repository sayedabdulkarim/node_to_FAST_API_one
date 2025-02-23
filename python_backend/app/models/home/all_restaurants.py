from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

class ImageBadge(BaseModel):
    imageId: str
    description: str

class TextExtendedBadge(BaseModel):
    iconId: str
    shortDescription: str
    fontColor: str

class Badges(BaseModel):
    imageBadges: List[ImageBadge]
    textExtendedBadges: List[TextExtendedBadge]

class Sla(BaseModel):
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

class Restaurant(BaseModel):
    aggregatedDiscountInfoV3: AggregatedDiscountInfoV3
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
    sla: Sla
    totalRatingsString: str
    type: str
    veg: bool
    adminUserId: str
