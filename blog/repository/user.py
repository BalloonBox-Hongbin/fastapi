from sqlalchemy.orm import Session
from fastapi import Depends, status, Response, HTTPException
from .. import models, schemas, hashing



def get_user(user_id,db:Session):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not avaiable")
    else:
        return user



def create_user(request:schemas.User,db:Session):
    new_user = models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
