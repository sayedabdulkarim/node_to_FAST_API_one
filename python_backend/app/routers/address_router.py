from fastapi import APIRouter, Depends, HTTPException
from typing import List
from bson import ObjectId
from ..models.address import AddressModel, AddressCreate
from ..utils.auth import verify_token
from ..config.database import get_database

router = APIRouter()

@router.post("/add")
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
    await db.addresses.create_index([("location", "2dsphere")])
    
    created_address = await db.addresses.find_one({"_id": result.inserted_id})
    created_address["_id"] = str(created_address["_id"])
    created_address["user"] = str(created_address["user"])
    
    return {"status": "success", "data": created_address}

@router.get("/user")
async def get_user_addresses(user_id: str = Depends(verify_token)):
    db = get_database()
    addresses = []
    
    async for address in db.addresses.find({"user": ObjectId(user_id)}):
        address["_id"] = str(address["_id"])
        address["user"] = str(address["user"])
        addresses.append(address)
    
    return {"status": "success", "data": addresses}

@router.delete("/{address_id}")
async def delete_address(address_id: str, user_id: str = Depends(verify_token)):
    db = get_database()
    result = await db.addresses.delete_one({
        "_id": ObjectId(address_id),
        "user": ObjectId(user_id)
    })
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Address not found")
    
    return {"status": "success", "message": "Address deleted successfully"}
