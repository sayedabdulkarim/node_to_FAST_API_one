import asyncio
import json
from motor.motor_asyncio import AsyncIOMotorClient
from ..config.database import DATABASE_URL
from ..models.restaurant_details import RestaurantDetails

async def seed_restaurant_details():
    try:
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client.get_default_database()
        
        json_path = "app/dummy_data/restaurantDetailsTable.json"
        with open(json_path, 'r') as file:
            restaurant_data = json.load(file)
        
        # Validate and convert data using Pydantic model
        validated_restaurants = []
        for restaurant in restaurant_data:
            try:
                restaurant_details = RestaurantDetails(**restaurant)
                validated_restaurants.append(restaurant_details.dict())
            except Exception as e:
                print(f"Validation error for restaurant: {restaurant.get('restaurantId', 'Unknown')}")
                print(f"Error: {str(e)}")
                continue
        
        if validated_restaurants:
            await db.restaurant_details.drop()
            result = await db.restaurant_details.insert_many(validated_restaurants)
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
    asyncio.run(seed_restaurant_details())
