from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get('/')
def index():
    response = {'data':
                    {
                    'name':'Hongbin'
                    }
            }
    return response

@app.get('/about')
def about():
    response = {'data':
                    [
                    'About Page'
                    ]
            }
    return response