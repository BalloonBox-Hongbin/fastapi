from fastapi import APIRouter
from .. import schemas,database,models, oauth2
from typing import List
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)



@router.get('/',status_code=status.HTTP_202_ACCEPTED,response_model=List[schemas.showBlog])
def get_all_blog(db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all_blogs(db)
        


@router.get('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.showBlog)
def get_blog(id:int,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_blog(id,db)




@router.post('/',status_code=status.HTTP_201_CREATED)
def post_blog(user_id:int,request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.post_blog(user_id,request,db)



@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.delete_blog(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int,request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update_blog(id,request,db)