from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    email: EmailStr
    phone: str
    favorites: List[PyObjectId] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True

class UserLogin(BaseModel):
    phone: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    token: str
