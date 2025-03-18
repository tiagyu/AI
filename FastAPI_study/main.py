from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"HELLO" : "WORLD"}

@app.get("/item/{item_id}")
def read_item(item_id : int, q : Union[str, None] = None):
    return {"item_id" : item_id, "q" : q}