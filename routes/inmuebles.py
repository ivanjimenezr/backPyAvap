from fastapi import APIRouter
from db.client import db_inmuebles
from schemas.inmuebles import inmuebleEntity, inmueblesEntity
from models.inmuebles import InmuebleModel
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



    

# Servicio para devolver inmueble por ID - GET
# @inmuebles.get("/{id}")
# def get_inmueble(id):
#     inmueble = client.db_inmuebles.get(id)
#     if inmueble: # Si encuentra inmueble
#         return inmueble
#     else: # Si no lo encuentra
#         return JSONResponse({"message":"Inmueble not found"}, status_code=404)

#Servicio para devolver todos los registros - GET
@inmuebles.get("/inmuebles")
def list_inmuebles():
    inmuebles = inmueblesEntity(db_inmuebles.find())
    
    return  inmuebles
 
# Servicio para UPDATE inmueble por ID - PATCH
# @inmuebles.patch("/{uid}")
# def update_inmueble(uid: str, uu: InmuebleUpdate):
#     updates = {k:v for k,v in uu.dict().items() if v is not None}
#     try:
#         client.db.update(updates,uid)
#         return client.db_inmuebles.get(uid)
#     except Exception:
#         return JSONResponse({"message":"Inmueble not found"}, status_code=404)

# Serviciopara crear inmueble - POST
# @inmuebles.post("/", status_code=201)
# def create_inmueble(inmueble: Inmueble):
#     inmueble = inmueble.json()
#     print(inmueble)
#     print(type(inmueble))
#     inmuebleJson = json.loads(inmueble) 
#     print('despues de convertir: ',type(inmueble))

#     u = client.db_inmuebles.put(inmuebleJson)
#     return u

# Servicio para borrar un inmueble por ID - DELETE
# @inmuebles.delete("/{id}")
# def delete_inmueble(id:str):
#     try:
#         client.db_inmuebles.delete(id)
#         return JSONResponse({"message":"Inmueble deleted"}, status_code=200)
#     except Exception:
#         return JSONResponse({"message":"Inmueble not found"}, status_code=404)
