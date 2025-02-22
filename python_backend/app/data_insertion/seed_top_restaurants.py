import json
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

async def seed_top_restaurants():
    # Connect to MongoDB
    client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    db = client.swiggy_one

    # Read JSON data
    with open("app/dummy_data/topRestaurantsTable.json") as f:
        restaurants_data = json.load(f)

    # Insert data into MongoDB
    try:
        await db.TopRestaurants.drop()  # Clear existing data
        result = await db.TopRestaurants.insert_many(restaurants_data)
        print(f"Successfully inserted {len(result.inserted_ids)} restaurants")
    except Exception as e:
        print(f"Error inserting restaurants: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(seed_top_restaurants())
