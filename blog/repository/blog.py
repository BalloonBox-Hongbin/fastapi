from sqlalchemy.orm import Session
from fastapi import Depends, status, Response, HTTPException
from .. import models, schemas



def get_all_blogs(db:Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blogs are not avaiable")
    else:
        return blogs



def get_blog(id,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not avaiable")
    else:
        return blog



def post_blog(user_id,request:schemas.Blog,db:Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



def delete_blog(blog_id,db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id==blog_id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not found")
    else:
        blogs.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)



def update_blog(blog_id,repuest:schemas.Blog,db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id==blog_id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not found")
    else:
        blogs.update({'title':repuest.title,'body':repuest.body})
        db.commit()
        return 'updated'