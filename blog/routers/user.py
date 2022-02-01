from fastapi import APIRouter
from .. import schemas,database,models,hashing
from typing import List
from fastapi import Depends, status, Response, HTTPException
from .. import schemas,database,models, oauth2
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=["Users"]
)


@router.get('/{id}',status_code=status.HTTP_201_CREATED,response_model=schemas.showUser)
def get_user(id:int,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return user.get_user(id,db)



@router.post('/',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.showUser)
def create_user(request:schemas.User,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return user.create_user(request,db)