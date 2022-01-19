from typing import Optional
from fastapi import FastAPI

from blog import schemas
from blog import models,schemas
from blog.database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get('/blog')
def index(limits:int=11,published:bool=True,sort:Optional[str]=None):
    if published:
        response = {'data': f'{limits} blogs from the db sort {sort}'
                }
    else:
        response = {'data': 'The blogs are not published.'}
    return response



@app.post('/blog')
def post_blog(blog:schemas.Blog):
    return blog


# @app.get('/blog/unpublished')
# def unpublished():
#     response = {
#         'data':'All unpublished blogs'
#         }
#     return response

# @app.get('/blog/{id}')
# def show(id:int):
#     response = {
#         'data':{
#             'id':id
#         }
#         }
#     return response

# @app.get('/blog/{id}/comments')
# def comments(id,limit=10):
#     response = {
#         'data':{
#             'id':id,
#             'comments':'This is blog {} limit {}'.format(id,limit)
#         }
#         }
#     return response




# if __name__ == '__main__':
#     uvicorn.run(app,host='127.0.0.1',port=9000,debug=True)
