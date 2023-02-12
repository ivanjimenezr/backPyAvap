from fastapi import APIRouter,status, Response
from db.client import db_inmuebles
from schemas.inmuebles import inmuebleEntity, inmueblesEntity
from models.inmuebles import InmuebleModel
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
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

inmuebles = APIRouter()

# deta = Deta() 

# db = deta.Base('inmuebles') #Nombrepara la bbdd

# app = FastAPI()

# origins = ["*"]

# inmuebles.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# @inmuebles.get("/inmuebles")
# def read_root():
#     return {"Hello": "World2"}

#Servicio para devolver todos los registros - GET
@inmuebles.get("/inmuebles")
async def list_inmuebles():
    # inmuebles = db_inmuebles.find()
    
    return  inmueblesEntity(db_inmuebles.find())


# Serviciopara crear inmueble - POST
@inmuebles.post("/inmuebles", response_model=InmuebleModel)
async def create_inmueble(inmueble: InmuebleModel):
    inmueble_dic = dict(inmueble)
    # del inmueble_dic['id']
    id = db_inmuebles.insert_one(inmueble_dic).inserted_id
    new_inmueble = db_inmuebles.find_one({"_id": id})
    return inmuebleEntity(new_inmueble)
    

# Servicio para devolver inmueble por ID - GET
@inmuebles.get("/inmuebles/{id}")
async def get_inmueble(id:str):
    return inmuebleEntity( db_inmuebles.find_one({"_id": ObjectId(id)}))

# Servicio para borrar un inmueble por ID - DELETE
@inmuebles.delete("/inmuebles/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inmueble(id:str):
    found =  db_inmuebles.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"error":"No se ha borrado el inmueble"}

# Servicio para actualizar inmueble por ID - GET
@inmuebles.put("/inmuebles/{id}")
async def up_inmueble(id:str, inmueble:InmuebleModel):
    db_inmuebles.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(inmueble)})
    return inmuebleEntity( db_inmuebles.find_one({"_id": ObjectId(id)}))

# Servicio para UPDATE inmueble por ID - PATCH
# @inmuebles.patch("/{uid}")
# def update_inmueble(uid: str, uu: InmuebleUpdate):
#     updates = {k:v for k,v in uu.dict().items() if v is not None}
#     try:
#         client.db.update(updates,uid)
#         return client.db_inmuebles.get(uid)
#     except Exception:
#         return JSONResponse({"message":"Inmueble not found"}, status_code=404)


