from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class OfferInfo(BaseModel):
    header: Optional[str]
    offerTagColor: Optional[str]
    offerIds: Optional[List[str]]
    expiryTime: Optional[str]
    couponCode: Optional[str]
    description: Optional[str]
    offerType: Optional[str]
    restId: Optional[str]
    offerLogo: Optional[str]
    descriptionTextColor: Optional[str]
    offerTag: Optional[str]
    logoBottom: Optional[str]

class OfferCTA(BaseModel):
    type: Optional[str]

class Offer(BaseModel):
    info: Optional[OfferInfo]
    cta: Optional[OfferCTA]

class ItemRatings(BaseModel):
    rating: Optional[float]
    ratingCount: Optional[int]

class ItemAttributes(BaseModel):
    vegClassifier: Optional[str]

class MenuItem(BaseModel):
    id: str
    name: str
    description: Optional[str]
    imageId: Optional[str]
    inStock: Optional[bool]
    price: Optional[float]
    variants: Optional[List[Dict[str, Any]]]
    attributes: Optional[ItemAttributes]
    ratings: Optional[ItemRatings]
    offers: Optional[List[Offer]]

class MenuCategory(BaseModel):
    categoryName: str
    items: List[MenuItem]

class RestaurantDetails(BaseModel):
    restaurantId: str
    menu: List[MenuCategory]
