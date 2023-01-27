from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
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

class UserUpdate(BaseModel): # Clase para el update
    name: str = None
    age: int = None
    hometown: str = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Srviciopara crear dato - POST
@app.post("/users", status_code=201)
def create_user(user: User):
    u = db.put(user.dict())
    return u

# Servicio para devolver dato por ID - GET
@app.get("/users/{id}")
def create_user(id):
    user = db.get(id)
    if user: # Si encuentra usuario
        return user
    else: # Si no lo encuentra
        return JSONResponse({"message":"user not found"}, status_code=404)

#Servicio para devolver todos los registros - GET
@app.get("/users/")
def view_users():
    user = db.fetch()
    json_compatible_item_data = jsonable_encoder(user)
    return  JSONResponse(content=json_compatible_item_data['_items'])
 
# Servicio para UPDATE dato por ID - PATCH
@app.patch("/users/{uid}")
def update_user(uid: str, uu: UserUpdate):
    updates = {k:v for k,v in uu.dict().items() if v is not None}
    try:
        db.update(updates,uid)
        return db.get(uid)
    except Exception:
        return JSONResponse({"message":"user not found"}, status_code=404)

# Servicio para borrar dato por ID - DELETE
@app.delete("/users/{id}")
def delete_user(id:str):
    try:
        db.delete(id)
        return JSONResponse({"message":"user deleted"}, status_code=200)
    except Exception:
        return JSONResponse({"message":"user not found"}, status_code=404)
