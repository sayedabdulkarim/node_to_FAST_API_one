from fastapi import APIRouter, Depends, HTTPException, Body
from typing import Dict
from bson import ObjectId
from ..models.user import UserModel, UserLogin, UserCreate, UserResponse
from ..utils.auth import create_access_token, verify_token
from ..config.database import get_database

router = APIRouter()

@router.get("/")
async def get_users():
    return {"message": "Users endpoint"}

@router.post("/signup", response_model=Dict)
async def user_signup(user: UserCreate):
    db = get_database()
    # Check if user exists
    if await db.users.find_one({"phone": user.phone}):
        raise HTTPException(400, "User with this phone number already exists")
    if await db.users.find_one({"email": user.email}):
        raise HTTPException(400, "User with this email already exists")

    # Create new user
    new_user = UserModel(
        name=user.name,
        email=user.email,
        phone=user.phone,
        favorites=[]
    ).dict(exclude_none=True)
    
    result = await db.users.insert_one(new_user)
    token = create_access_token(str(result.inserted_id))
    
    return {
        "message": "User registered successfully",
        "user": {
            "name": user.name,
            "email": user.email,
            "phone": user.phone
        },
        "token": token
    }

@router.post("/login")
async def user_login(user_data: UserLogin):
    db = get_database()
    user = await db.users.find_one({"phone": user_data.phone})
    if not user:
        raise HTTPException(404, "User not found")
    
    token = create_access_token(str(user["_id"]))
    
    return {
        "token": token,
        "data": {
            "_id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "phoneNumber": user["phone"],
            "favorites": [str(fav) for fav in user.get("favorites", [])]
        },
        "message": "Login successful"
    }

@router.get("/profile")
async def get_user_profile(user_id: str = Depends(verify_token)):
    db = get_database()
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(404, "User not found")
    
    return {
        "_id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }

@router.put("/profile")
async def update_user_profile(
    updated_data: dict = Body(...),
    user_id: str = Depends(verify_token)
):
    db = get_database()
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(404, "User not found")

    if "email" in updated_data:
        existing_email = await db.users.find_one({
            "email": updated_data["email"],
            "_id": {"$ne": ObjectId(user_id)}
        })
        if existing_email:
            raise HTTPException(400, "Email already in use")

    update_fields = {}
    if "name" in updated_data:
        update_fields["name"] = updated_data["name"]
    if "email" in updated_data:
        update_fields["email"] = updated_data["email"]

    if update_fields:
        await db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_fields}
        )
        
    updated_user = await db.users.find_one({"_id": ObjectId(user_id)})
    return {
        "id": str(updated_user["_id"]),
        "name": updated_user["name"],
        "email": updated_user["email"]
    }
