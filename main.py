from fastapi import FastAPI
from pydantic import BaseModel
from deta import Deta

# Levantar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# DETA INSTRUCTIONS
# deta visor open //para abrir la consola
# deta watch // deploy automaticamente los cambios
# deta --help

deta = Deta() 

db = deta.Base('fastapi-crud')

app = FastAPI() 

class User(BaseModel):
    name: str
    age: int
    hometown: str

# @app.get("/") 
# async def root():
#     return {"Hello": "there"}

# @app.get("/url")
# async def root():
#     return {"Hello": "World2"}

@app.post("/users", status_code=201)
def create_user(user:User):
    u = db.put(user.dict())
    return u

@app.get("/users")
def view_user():
    us = next(db.fetch())
    return us

