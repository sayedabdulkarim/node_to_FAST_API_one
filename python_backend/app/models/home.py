from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BestOffer(BaseModel):
    image: str
    title: str
    description: Optional[str] = None

class Restaurant(BaseModel):
    name: str
    image: str
    cuisine: str
    rating: float
    delivery_time: str
    price_for_two: float

class Cuisine(BaseModel):
    name: str
    image: str

class HomePageResponse(BaseModel):
    offer_list: List[BestOffer]
    top_restaurant_list: List[Restaurant]
    cuisines_list: List[Cuisine]
    all_restaurants_list: List[Restaurant]
