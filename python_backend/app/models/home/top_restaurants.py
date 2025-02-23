from pydantic import BaseModel
from typing import List, Optional

class AggregatedDiscountInfoV3(BaseModel):
    header: str
    subHeader: str

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
