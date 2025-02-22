from fastapi import APIRouter, Depends, HTTPException, Body
from typing import List
from bson import ObjectId
from ..models.address import AddressModel, AddressCreate
from ..utils.auth import verify_token
from ..config.database import get_database

router = APIRouter()

@router.post("/addAddress")
async def add_address(
    address_data: AddressCreate,
    user_id: str = Depends(verify_token)
):
    db = get_database()
    
    new_address = AddressModel(
        user=ObjectId(user_id),
        address=address_data.address,
        doorNumber=address_data.doorNumber,
        landmark=address_data.landmark,
        location=address_data.location,
        type=address_data.type
    ).dict(exclude_none=True)
    
    result = await db.addresses.insert_one(new_address)
    
    # Create geospatial index if it doesn't exist
    await db.addresses.create_index([("location", "2dsphere")])
    
    created_address = await db.addresses.find_one({"_id": result.inserted_id})
    created_address["_id"] = str(created_address["_id"])
    created_address["user"] = str(created_address["user"])
    
    return {
        "message": "Address added successfully",
        "address": created_address
    }

@router.get("/getAddressesByUser")
async def get_addresses_by_user(user_id: str = Depends(verify_token)):
    db = get_database()
    
    addresses = []
    cursor = db.addresses.find({"user": ObjectId(user_id)})
    
    async for address in cursor:
        address["_id"] = str(address["_id"])
        address["user"] = str(address["user"])
        addresses.append(address)
    
    return {
        "message": "Addresses retrieved successfully",
        "addresses": addresses
    }
