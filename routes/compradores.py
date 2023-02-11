from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from pydantic import BaseModel
from deta import Deta
from db import client
from db.models.compradores import Comprador, CompradorUpdate

### Compradores API ###

# Levantar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# DETA INSTRUCTIONS
# deta visor open //para abrir la consola
# deta watch // deploy automaticamente los cambios
# deta --help

router = APIRouter(prefix="/compradores",
                   tags=["compradores"],
                   responses={404: {"message": "Comprador No encontrado"}})



# Serviciopara crear inmueble - POST
@router.post("/", status_code=201)
def create_inmueble(inmueble: Comprador):
    u = client.db.put(inmueble.dict())
    return u

# Servicio para devolver comprador por ID - GET
@router.get("/{id}")
def get_comprador(id):
    comprador = client.db.get(id)
    if comprador: # Si encuentra inmueble
        return comprador
    else: # Si no lo encuentra
        return JSONResponse({"message":"comprador not found"}, status_code=404)

#Servicio para devolver todos los registros - GET
@router.get("/")
def get_comprador():
    comprador = client.db.fetch()
    json_compatible_item_data = jsonable_encoder(comprador)
    return  JSONResponse(content=json_compatible_item_data['_items'])
 
# Servicio para UPDATE inmueble por ID - PATCH
@router.patch("/{uid}")
def update_comprador(uid: str, uu: CompradorUpdate):
    updates = {k:v for k,v in uu.dict().items() if v is not None}
    try:
        client.db.update(updates,uid)
        return client.db.get(uid)
    except Exception:
        return JSONResponse({"message":"comprador not found"}, status_code=404)

# Servicio para borrar un inmueble por ID - DELETE
@router.delete("/{id}")
def delete_comprador(id:str):
    try:
        client.db.delete(id)
        return JSONResponse({"message":"comprador deleted"}, status_code=200)
    except Exception:
        return JSONResponse({"message":"comprador not found"}, status_code=404)
