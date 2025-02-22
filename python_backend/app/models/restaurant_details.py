from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Rating(BaseModel):
    rating: Optional[str] = None
    ratingCount: Optional[str] = None
    ratingCountV2: Optional[str] = None

class ItemAttribute(BaseModel):
    vegClassifier: str

class MenuItem(BaseModel):
    offers: List[Dict] = []
    id: str
    description: str
    name: str
    imageId: str
    inStock: int
    price: int
    variants: Dict = {}
    variantsV2: Dict = {}
    itemAttribute: ItemAttribute
    ribbon: Dict = {}
    type: str
    itemBadge: Dict = {}
    badgesV2: Dict = {}
    ratings: Dict[str, Any] = {}

class MenuCategory(BaseModel):
    categoryName: str
    items: List[MenuItem]

class RestaurantDetails(BaseModel):
    restaurantId: str
    menu: List[MenuCategory]
