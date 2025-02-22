import asyncio
import json
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from ..config.database import DATABASE_URL

# Sample admin user ID - you should replace this with a real admin ID
DEFAULT_ADMIN_ID = ObjectId()

async def seed_restaurants():
    try:
        # Connect to MongoDB
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client.get_default_database()
        
        # Read restaurants from JSON file
        json_path = "../dummy_data/allRestaurantsTable.json"
        with open(json_path, 'r') as file:
            all_restaurants_data = json.load(file)
        
        # Add admin user ID to each restaurant
        restaurants_with_admin = [
            {**restaurant, "adminUserId": DEFAULT_ADMIN_ID}
            for restaurant in all_restaurants_data
        ]
        
        # Insert restaurants
        result = await db.restaurants.insert_many(restaurants_with_admin)
        print(f"Successfully inserted {len(result.inserted_ids)} restaurants")
        
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
