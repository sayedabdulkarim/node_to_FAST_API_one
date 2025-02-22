import asyncio
import json
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from ..config.database import DATABASE_URL
from ..models.restaurant import Restaurant
from ..models.menu import Menu
from typing import List

DEFAULT_ADMIN_ID = ObjectId()

async def seed_restaurants():
    try:
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client.get_default_database()
        
        json_path = "../dummy_data/allRestaurantsTable.json"
        with open(json_path, 'r') as file:
            all_restaurants_data = json.load(file)
        
        # Validate and convert data using Pydantic model
        validated_restaurants = []
        for restaurant_data in all_restaurants_data:
            try:
                # Add admin user ID to each restaurant
                restaurant_data["adminUserId"] = DEFAULT_ADMIN_ID
                # Validate using Restaurant model
                restaurant = Restaurant(**restaurant_data)
                validated_restaurants.append(restaurant.dict())
            except Exception as e:
                print(f"Validation error for restaurant: {restaurant_data.get('name', 'Unknown')}")
                print(f"Error: {str(e)}")
                continue
        
        if validated_restaurants:
            result = await db.restaurants.insert_many(validated_restaurants)
            print(f"Successfully inserted {len(result.inserted_ids)} restaurants")
        else:
            print("No valid restaurants to insert")
        
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_path}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(seed_restaurants())
