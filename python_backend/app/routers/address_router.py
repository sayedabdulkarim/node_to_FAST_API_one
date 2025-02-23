from fastapi import APIRouter, Depends, HTTPException
from typing import List
from bson import ObjectId
from datetime import datetime
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
    
    # Create new address document
    new_address = AddressModel(
        user=ObjectId(user_id),
        address=address_data.address,
        doorNumber=address_data.doorNumber,
        landmark=address_data.landmark,
        location=address_data.location,
        type=address_data.type
    ).dict(exclude_none=True)
    
    # Create geospatial index for location field
    await db.addresses.create_index([("location", "2dsphere")])
    
    # Insert the new address
    result = await db.addresses.insert_one(new_address)
    
    # Fetch and return the created address
    created_address = await db.addresses.find_one({"_id": result.inserted_id})
    created_address["_id"] = str(created_address["_id"])
    created_address["user"] = str(created_address["user"])
    
    return {"status": "success", "message": "Address added successfully", "data": created_address}

@router.get("/all")
async def get_user_addresses(user_id: str = Depends(verify_token)):
    db = get_database()
    addresses = []
    
    async for address in db.addresses.find({"user": ObjectId(user_id)}):
        address["_id"] = str(address["_id"])
        address["user"] = str(address["user"])
        addresses.append(address)
    
    return {"status": "success", "data": addresses}

@router.delete("/{address_id}")
async def delete_address(
    address_id: str, 
    user_id: str = Depends(verify_token)
):
    db = get_database()
    
    # Verify address exists and belongs to user
    address = await db.addresses.find_one({
        "_id": ObjectId(address_id),
        "user": ObjectId(user_id)
    })
    
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    
    # Delete the address
    await db.addresses.delete_one({
        "_id": ObjectId(address_id),
        "user": ObjectId(user_id)
    })
    
    return {"status": "success", "message": "Address deleted successfully"}

@router.put("/{address_id}")
async def update_address(
    address_id: str,
    address_data: AddressCreate,
    user_id: str = Depends(verify_token)
):
    db = get_database()
    
    # Verify address exists and belongs to user
    address = await db.addresses.find_one({
        "_id": ObjectId(address_id),
        "user": ObjectId(user_id)
    })
    
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    
    # Update the address
    update_data = address_data.dict(exclude_none=True)
    update_data["updated_at"] = datetime.now()
    
    await db.addresses.update_one(
        {"_id": ObjectId(address_id)},
        {"$set": update_data}
    )
    
    # Fetch and return updated address
    updated_address = await db.addresses.find_one({"_id": ObjectId(address_id)})
    updated_address["_id"] = str(updated_address["_id"])
    updated_address["user"] = str(updated_address["user"])
    
    return {"status": "success", "message": "Address updated successfully", "data": updated_address}
