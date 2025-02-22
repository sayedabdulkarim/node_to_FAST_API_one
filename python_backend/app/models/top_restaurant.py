from typing import List, Optional
from pydantic import BaseModel

class AggregatedDiscountInfoV3(BaseModel):
    header: Optional[str] = None
    subHeader: Optional[str] = None
    discountTag: Optional[str] = None

class TopRestaurant(BaseModel):
    name: str
    cloudinaryImageId: str
    locality: str
    areaName: str
    costForTwo: str
    cuisines: List[str]
    avgRating: float
    avgRatingString: str
    totalRatingsString: str
    badges: bool
    aggregatedDiscountInfoV3: AggregatedDiscountInfoV3
