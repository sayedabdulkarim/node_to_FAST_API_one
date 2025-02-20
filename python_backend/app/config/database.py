import os
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from dotenv import load_dotenv

load_dotenv()

mongo_client: AsyncIOMotorClient = None
db: AsyncIOMotorDatabase = None

async def connect_to_mongo():
    global mongo_client, db
    mongo_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    mongo_client = AsyncIOMotorClient(mongo_url)
    try:
        await mongo_client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        db = mongo_client[os.getenv("MONGODB_DB", "swiggy_one")]
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e

async def close_mongo_connection():
    global mongo_client
    if mongo_client:
        mongo_client.close()

def get_database() -> AsyncIOMotorDatabase:
    if db is None:
        raise Exception("Database not initialized")
    return db
