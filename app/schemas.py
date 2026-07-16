from pydantic import BaseModel, EmailStr
from datetime import datetime

#user schemes

class usercreate(BaseModel):
    full_name:str
    email:EmailStr
    password:str

class userlogin(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    full_name:str
    email:EmailStr
    created:datetime

    class Config:
        from_attributes = True

#JWT Token schemes

class Token(BaseModel):
    access_token:str
    token_type:str

class tokenData(BaseModel):
    email: str | None=None

#Task Schemes

class TaskCreate(BaseModel):
    title:str
    description:str
    status:str
class Taskupdate(BaseModel):
    title:str
    description:str
    status:str
class TaskResponse(BaseModel):
    id:int
    title:str
    description:str
    status:str
    user_id:int

    class Config:
        from_attributes =True

#uvicorn app.main:app --reload