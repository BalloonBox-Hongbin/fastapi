from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas,database,models,hashing,token
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime,timedelta

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not hashing.Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Password")
    access_token = token.create_access_token(data={"sub": user.email},expires_delta=timedelta(days=1))
    return {"access_token": access_token, "token_type": "bearer"}