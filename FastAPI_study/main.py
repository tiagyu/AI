from fastapi import FastAPI
from pydantic import BaseModel
from controller import items, users

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"HELLO" : "WORLD"}

@app.get("/routes")
def get_routes():
    return [{"path": route.path, "name": route.name} for route in app.routes]