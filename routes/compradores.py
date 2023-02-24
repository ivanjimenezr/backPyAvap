from fastapi import APIRouter,status, Response,Depends
from fastapi.responses import FileResponse
from db.client import db_compradores
from schemas.compradores import compradorEntity, compradoresEntity
from models.compradores import CompradorModel
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
# from starlette.responses import FileResponse

from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer



# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# from deta import Deta
# from db import client
# import json

### Inmuebles API ###

# Levantar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# DETA INSTRUCTIONS
# deta visor open //para abrir la consola
# deta watch // deploy automaticamente los cambios
# deta --help 

compradores = APIRouter()

# deta = Deta() 

# db = deta.Base('inmuebles') #Nombrepara la bbdd

# app = FastAPI()




# @inmuebles.get("/inmuebles")
# def read_root():
#     return {"Hello": "World2"}

#Servicio para devolver todos los registros - GET
@compradores.get("/compradores", dependencies=[Depends(JWTBearer())], tags=["compradores"])
async def list_compradores():
    return  compradoresEntity(db_compradores.find())


# Serviciopara crear compradores - POST
@compradores.post("/compradores", response_model=CompradorModel, dependencies=[Depends(JWTBearer())], tags=["compradores"])
async def create_comprador(comprador: CompradorModel):
    comprador_dic = dict(comprador)
    id = db_compradores.insert_one(comprador_dic).inserted_id
    new_inmueble = db_compradores.find_one({"_id": id})
    return compradorEntity(new_inmueble)
    

# Servicio para devolver comprador por ID - GET
@compradores.get("/compradores/{id}", dependencies=[Depends(JWTBearer())], tags=["compradores"])
async def get_comprador(id:str):
    return compradorEntity( db_compradores.find_one({"_id": ObjectId(id)}))

# Servicio para borrar un comprador por ID - DELETE
@compradores.delete("/compradores/{id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())], tags=["compradores"])
def delete_comprador(id:str):
    found =  db_compradores.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"error":"No se ha borrado el comprador"}

# Servicio para actualizar comprador por ID - GET
@compradores.put("/compradores/{id}", dependencies=[Depends(JWTBearer())], tags=["compradores"])
async def up_comprador(id:str, comprador:CompradorModel):
    req = {k: v for k, v in comprador.dict().items() if v is not None}
    db_compradores.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(req)})
    return compradorEntity( db_compradores.find_one({"_id": ObjectId(id)}))

# Servicio para finalizar comprador por ID - GET
@compradores.patch("/compradores/{id}", dependencies=[Depends(JWTBearer())], tags=["compradores"])
async def finalizar_comprador(id:str, compradorFin:CompradorModel):
    req = {k: v for k, v in compradorFin.dict().items() if v is not None}
    db_compradores.find_one_and_update({"_id": ObjectId(id)},{"$set":req})
    return compradorEntity( db_compradores.find_one({"_id": ObjectId(id)}))
