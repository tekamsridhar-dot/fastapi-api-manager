from datetime import datetime, timedelta

from jose import JWTError,jwt
from passlib.context import CryptContext

from .config import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES

# PWD HASHING
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_password_hash(password:str):
    return  pwd_context.hash(password)

#To verify password
def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

#to create JWT  TOKEN
def create_access_token(data: dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

#Decade JWT tOKEN
def decode_access_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    
    