from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from pydantic import BaseModel
from deta import Deta
from db import client
from db.models.vendedores import Vendedor, VendedorUpdate 

### Compradores API ###

# Levantar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# DETA INSTRUCTIONS
# deta visor open //para abrir la consola
# deta watch // deploy automaticamente los cambios
# deta --help

router = APIRouter(prefix="/vendedores",
                   tags=["vendedores"],
                   responses={404: {"message": "Vendedor No encontrado"}})



# Serviciopara crear inmueble - POST
@router.post("/", status_code=201)
def create_vendedor(inmueble: Vendedor):
    u = client.db.put(inmueble.dict())
    return u

# Servicio para devolver Vendedor por ID - GET
@router.get("/{id}")
def get_vendedor(id):
    vendedor = client.db.get(id)
    if vendedor: # Si encuentra vendedor
        return vendedor
    else: # Si no lo encuentra
        return JSONResponse({"message":"Vendedor not found"}, status_code=404)

#Servicio para devolver todos los registros - GET
@router.get("/")
def get_vendedor():
    vendedor = client.db.fetch()
    json_compatible_item_data = jsonable_encoder(vendedor)
    return  JSONResponse(content=json_compatible_item_data['_items'])
 
# Servicio para UPDATE Vendedor por ID - PATCH
@router.patch("/{uid}")
def update_vendedor(uid: str, uu: VendedorUpdate):
    updates = {k:v for k,v in uu.dict().items() if v is not None}
    try:
        client.db.update(updates,uid)
        return client.db.get(uid)
    except Exception:
        return JSONResponse({"message":"Vendedor not found"}, status_code=404)

# Servicio para borrar un Vendedor por ID - DELETE
@router.delete("/{id}")
def delete_vendedor(id:str):
    try:
        client.db.delete(id)
        return JSONResponse({"message":"Vendedor deleted"}, status_code=200)
    except Exception:
        return JSONResponse({"message":"Vendedor not found"}, status_code=404)
