import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

mongo_client = None
db = None

async def connect_to_mongo():
    global mongo_client, db
    mongo_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    mongo_client = AsyncIOMotorClient(mongo_url)
    try:
        await mongo_client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        db = get_database()
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e

async def close_mongo_connection():
    global mongo_client
    if mongo_client:
        mongo_client.close()

def get_database():
    db_name = os.getenv("MONGODB_DB", "swiggy_one")
    return mongo_client[db_name]
