from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from pydantic import BaseModel
from deta import Deta
from db import client
from db.models.inmuebles import Inmueble, InmuebleUpdate

### Inmuebles API ###

# Levantar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# DETA INSTRUCTIONS
# deta visor open //para abrir la consola
# deta watch // deploy automaticamente los cambios
# deta --help

router = APIRouter(prefix="/inmuebles",
                   tags=["inmuebles"],
                   responses={404: {"message": "Inmueble No encontrado"}})

# deta = Deta() 

# db = deta.Base('inmuebles') #Nombrepara la bbdd

# app = FastAPI()

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# @router.get("/")
# def read_root():
#     return {"Hello": "World"}

# Serviciopara crear inmueble - POST
@router.post("/", status_code=201)
def create_inmueble(inmueble: Inmueble):
    u = client.db.put(inmueble.dict())
    return u

# Servicio para devolver inmueble por ID - GET
@router.get("/{id}")
def get_inmueble(id):
    inmueble = client.db.get(id)
    if inmueble: # Si encuentra inmueble
        return inmueble
    else: # Si no lo encuentra
        return JSONResponse({"message":"Inmueble not found"}, status_code=404)

#Servicio para devolver todos los registros - GET
@router.get("/")
def get_inmuebles():
    inmueble = client.db.fetch()
    json_compatible_item_data = jsonable_encoder(inmueble)
    return  JSONResponse(content=json_compatible_item_data['_items'])
 
# Servicio para UPDATE inmueble por ID - PATCH
@router.patch("/{uid}")
def update_inmueble(uid: str, uu: InmuebleUpdate):
    updates = {k:v for k,v in uu.dict().items() if v is not None}
    try:
        client.db.update(updates,uid)
        return client.db.get(uid)
    except Exception:
        return JSONResponse({"message":"Inmueble not found"}, status_code=404)

# Servicio para borrar un inmueble por ID - DELETE
@router.delete("/{id}")
def delete_inmueble(id:str):
    try:
        client.db.delete(id)
        return JSONResponse({"message":"Inmueble deleted"}, status_code=200)
    except Exception:
        return JSONResponse({"message":"Inmueble not found"}, status_code=404)
