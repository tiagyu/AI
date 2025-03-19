from fastapi import FastAPI
from pydantic import BaseModel
from controller import items, users

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"HELLO" : "My name is Roh"}