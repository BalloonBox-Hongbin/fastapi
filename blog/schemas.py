from turtle import title
from pydantic import BaseModel
from typing import Optional, List



class Login(BaseModel):
    username:str
    password:str



class BlogBase(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode = True



class Blog(BlogBase):
    class Config():
        orm_mode = True



class User(BaseModel):
    name:str
    email:str
    password:str



class showUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True



class showUserBlog(showUser):
    blogs:List[Blog]=[]



class showBlog(BaseModel):
    title:str
    body:str
    creator:showUser
    class Config():
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str



class TokenData(BaseModel):
    email: Optional[str] = None