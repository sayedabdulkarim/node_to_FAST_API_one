from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from ..models.restaurant import RestaurantDetails
from ..utils.auth import verify_token
from ..config.database import get_database

router = APIRouter()

@router.get("/getRestaurantDetails/{restaurant_id}")
async def get_restaurant_details(
    restaurant_id: str,
    user_id: str = Depends(verify_token)
):
    db = get_database()
    
    # Fetch basic restaurant details
    restaurant = await db.restaurants.find_one({"_id": ObjectId(restaurant_id)})
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    
    # Fetch menu details
    menu = await db.restaurant_details.find_one({"restaurantId": restaurant_id})
    
    # Convert ObjectId to string
    restaurant["_id"] = str(restaurant["_id"])
    if menu:
        menu["_id"] = str(menu["_id"])
    
    return {
        "status": "success",
        "data": {
            **restaurant,
            "menu": menu
        },
        "message": "Restaurant details fetched successfully"
    }

@router.post("/addFavoriteRestaurant/{restaurant_id}")
async def add_favorite(
    restaurant_id: str,
    user_id: str = Depends(verify_token)
):
    db = get_database()
    
    # Add restaurant to user's favorites
    result = await db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"favorites": restaurant_id}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="Restaurant already in favorites")
    
    # Get updated user data
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    user["_id"] = str(user["_id"])
    
    return {
        "status": "success",
        "data": user,
        "message": "Restaurant added to favorites successfully"
    }

@router.delete("/removeFavoriteRestaurant/{restaurant_id}")
async def remove_favorite(
    restaurant_id: str,
    user_id: str = Depends(verify_token)
):
    db = get_database()
    
    # Remove restaurant from user's favorites
    result = await db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$pull": {"favorites": restaurant_id}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="Restaurant not in favorites")
    
    # Get updated user data
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    user["_id"] = str(user["_id"])
    
    return {
        "status": "success",
        "data": user,
        "message": "Restaurant removed from favorites successfully"
    }
