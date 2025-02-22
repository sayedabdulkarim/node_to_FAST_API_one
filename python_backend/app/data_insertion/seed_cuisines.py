import asyncio
import json
from motor.motor_asyncio import AsyncIOMotorClient
from ..config.database import DATABASE_URL
from ..models.cuisines import Cuisine

async def seed_cuisines():
    try:
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client.get_default_database()
        
        json_path = "app/dummy_data/filterCuisinesTable.json"
        with open(json_path, 'r') as file:
            cuisines_data = json.load(file)
        
        # Validate and convert data using Pydantic model
        validated_cuisines = []
        for cuisine_data in cuisines_data:
            try:
                cuisine = Cuisine(**cuisine_data)
                validated_cuisines.append(cuisine.dict())
            except Exception as e:
                print(f"Validation error for cuisine: {cuisine_data.get('label', 'Unknown')}")
                print(f"Error: {str(e)}")
                continue
        
        if validated_cuisines:
            await db.cuisines.drop()
            result = await db.cuisines.insert_many(validated_cuisines)
            print(f"Successfully inserted {len(result.inserted_ids)} cuisines")
        else:
            print("No valid cuisines to insert")
        
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_path}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(seed_cuisines())
