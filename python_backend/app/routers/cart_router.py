from fastapi import APIRouter, Depends, HTTPException
from ..models.cart import CartModel, CartCreate
from ..utils.auth import verify_token
from ..config.database import get_database
from bson import ObjectId

router = APIRouter()

@router.post("/addOrder")
async def add_order(
    order_data: CartCreate,
    user_id: str = Depends(verify_token)
):
    db = get_database()
    
    # Validate request data
    if not order_data.restaurantId or not order_data.addressDetails or \
       not order_data.items or not order_data.finalCost:
        raise HTTPException(status_code=400, detail="Missing order details")

    # Create new cart/order document
    new_order = CartModel(
        userId=ObjectId(user_id),
        restaurantId=ObjectId(order_data.restaurantId),
        addressDetails=order_data.addressDetails,
        items=order_data.items,
        finalCost=order_data.finalCost
    ).dict(exclude_none=True)

    # Save order to database
    result = await db.carts.insert_one(new_order)
    
    # Fetch and return created order
    saved_order = await db.carts.find_one({"_id": result.inserted_id})
    saved_order["_id"] = str(saved_order["_id"])
    saved_order["userId"] = str(saved_order["userId"])
    saved_order["restaurantId"] = str(saved_order["restaurantId"])
    
    return {
        "savedOrder": saved_order,
        "message": "Added successfully."
    }
