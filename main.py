'''
$ sudo pip3 install fastapi
$ pip install uvicorn[standard]
$ uvicorn main:app --reload
'''
from typing import Optional

from fastapi import FastAPI

import json

app = FastAPI()

#JSON SCHEME
#[{"item_id": int,
#  "value": int}]
with open('db.json') as json_file:
    db=json.load(json_file)


#@app.get("/")
def read_root():
    '''
    http://127.0.0.1:8000/ → db
    '''
    with open('db.json') as json_file:
        db=json.load(json_file)
    return db

@app.get("/")
def read_item(item_id: int = -1,value: int =-1):
    if item_id==-1:
        return db
    else:
        if value==-1:
            return [ d for d in db if d.get('item_id')==item_id ]
        else:
            return [ d for d in db if d.get('item_id')==item_id and d.get("value")==value ]


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    '''
    http://127.0.0.1:8000/items/6 → [{"item_id":6}]
    '''
    with open('db.json') as json_file:
        db=json.load(json_file)

    return [ d for d in db if d.get("item_id")==item_id ] #{"item_id": item_id, "q": q}


