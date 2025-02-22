import asyncio
import json
from motor.motor_asyncio import AsyncIOMotorClient
from ..config.database import DATABASE_URL
from ..models.best_offers import BestOffer

async def seed_best_offers():
    try:
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client.get_default_database()
        
        json_path = "app/dummy_data/bestOffersTable.json"
        with open(json_path, 'r') as file:
            offers_data = json.load(file)
        
        validated_offers = []
        for offer_data in offers_data:
            try:
                offer = BestOffer(**offer_data)
                validated_offers.append(offer.dict())
            except Exception as e:
                print(f"Validation error for offer: {offer_data.get('name', 'Unknown')}")
                print(f"Error: {str(e)}")
                continue
        
        if validated_offers:
            await db.bestoffers.drop()
            result = await db.bestoffers.insert_many(validated_offers)
            print(f"Successfully inserted {len(result.inserted_ids)} offers")
        else:
            print("No valid offers to insert")
        
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_path}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(seed_best_offers())
