from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os

security = HTTPBearer()

def create_access_token(user_id: str) -> str:
    try:
        payload = {
            'id': str(user_id),
            'exp': datetime.utcnow() + timedelta(days=2)
        }
        token = jwt.encode(payload, os.getenv('JWT_SECRET'), algorithm='HS256')
        return token
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
        return payload['id']
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
