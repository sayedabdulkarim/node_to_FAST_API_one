from fastapi import APIRouter, Depends
from typing import Dict
from ..utils.auth import verify_token
from ..config.database import get_database
from bson import ObjectId

router = APIRouter()

@router.get("/getHomePageData")
async def get_home_page_data(user_id: str = Depends(verify_token)):
    db = get_database()
    
    # Fetch data from collections
    offer_list = await db.best_offers.find().to_list(length=None)
    top_restaurant_list = await db.top_restaurants.find().to_list(length=None)
    cuisines_list = await db.cuisines.find().to_list(length=None)
    all_restaurants_list = await db.all_restaurants.find().to_list(length=None)
    user_order_details = await db.carts.find({"user_id": ObjectId(user_id)}).to_list(length=None)

    # Convert ObjectId to string in the results
    for restaurant in top_restaurant_list + all_restaurants_list:
        restaurant["_id"] = str(restaurant["_id"])
    
    for cuisine in cuisines_list:
        cuisine["_id"] = str(cuisine["_id"])
    
    for offer in offer_list:
        offer["_id"] = str(offer["_id"])
    
    for order in user_order_details:
        order["_id"] = str(order["_id"])
        order["user_id"] = str(order["user_id"])

    return {
        "data": {
            "offerList": offer_list,
            "topRestaurantList": top_restaurant_list,
            "cuisinesList": cuisines_list,
            "allRestaurantsList": all_restaurants_list,
            "userOrderDetails": user_order_details
        },
        "message": "done successfully"
    }
