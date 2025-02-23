from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routers import user_router, address_router, home_router
from app.config.database import connect_to_mongo, close_mongo_connection
import asyncio

load_dotenv()

app = FastAPI(title="Swiggy One API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

app.include_router(user_router.router, prefix="/api/users", tags=["users"])
app.include_router(address_router.router, prefix="/api/addresses", tags=["addresses"])
app.include_router(home_router.router, prefix="/api/home", tags=["home"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to Swiggy One API"}
