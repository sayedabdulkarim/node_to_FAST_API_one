from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class OfferInfo(BaseModel):
    header: str
    offerTagColor: str
    offerIds: List[str]
    expiryTime: str
    couponCode: str
    description: str
    offerType: str
    restId: str
    offerLogo: str
    descriptionTextColor: str
    offerTag: str
    logoBottom: str

class OfferCTA(BaseModel):
    type: str

class Offer(BaseModel):
    info: OfferInfo
    cta: OfferCTA

class ItemRatings(BaseModel):
    rating: float
    ratingCount: int

class ItemAttributes(BaseModel):
    vegClassifier: str

class MenuItem(BaseModel):
    id: str
    name: str
    description: Optional[str]
    imageId: Optional[str]
    inStock: bool
    price: float
    variants: List[Dict[str, Any]]
    attributes: ItemAttributes
    ratings: ItemRatings
    offers: List[Offer]

class MenuCategory(BaseModel):
    categoryName: str
    items: List[MenuItem]

class RestaurantDetails(BaseModel):
    restaurantId: str
    menu: List[MenuCategory]
