from fastapi import APIRouter,status, Response,BackgroundTasks,Depends
from fastapi.responses import FileResponse
# from db.client import db_vendedores
from schemas.vendedores import vendedorEntity, vendedoresEntity
from models.vendedores import VendedorModel
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
# from starlette.responses import FileResponse
import db.ConnToMysql as dataBase
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer

import pymysql.cursors
from dotenv import dotenv_values,load_dotenv
import os
import json

load_dotenv('.env') 

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

vendedores = APIRouter()

# deta = Deta() 

# db = deta.Base('inmuebles') #Nombrepara la bbdd

# app = FastAPI()




# @inmuebles.get("/inmuebles")
# def read_root():
#     return {"Hello": "World2"}

#Servicio para devolver todos los registros - GET
@vendedores.get("/vendedores")
async def list_vendedores():
    allVende = dataBase.get_all_vendedores()
    response = {
            "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
            },
            "statusCode": 200,
            'body': json.dumps(allVende)
            }
    return allVende

#Servicio para devolver vendedor por id - GET
@vendedores.get("/vendedores/{id}")
async def get_vendedores_id(id:int):
    vendedor = dataBase.get_vendedores_id(id)
    response = {
            "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
            },
            "statusCode": 200,
            'body': json.dumps(vendedor)
            }
    return vendedor
    # try:
    #     connection = pymysql.connect(
    #     host=os.environ.get("hostDB"),
    #     user=os.environ.get("userDB"),
    #     password=os.environ.get("passwordDB"),
    #     database=os.environ.get("databaseDB"),
    #     cursorclass=pymysql.cursors.DictCursor)

    #     with connection.cursor() as cursor:
            
    #         query = "SELECT * FROM avap.vendedores"
    #         cursor.execute(query)
    #         db = cursor.fetchall()
    #         print("Resultados de db: ", db)

    #         response = {
    #             "headers": {
    #             'Access-Control-Allow-Origin': '*',
    #             'Access-Control-Allow-Credentials': True
    #             },
    #             "statusCode": 200,
    #             'body': json.dumps(db)
    #             }
    #         return db
    # finally:
    #     cursor.close()
    #     connection.close()
    # return  vendedoresEntity(db_vendedores.find())

@vendedores.post("/vendedores/{id}")
async def vendedor(id:str, vendedor:VendedorModel):
    vendedor = dict(vendedor)
    db = dataBase.up_vendedor_id(id, vendedor)
    response = {
            "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
            },
            "statusCode": 200,
            'body': json.dumps({"status":"suscess", "result":f"El vendedor {id} se ha actualizado."})
            }
    return response
# Serviciopara crear vendedores - POST
# @vendedores.post("/vendedores", response_model=VendedorModel, dependencies=[Depends(JWTBearer())], tags=["vendedores"])
# @vendedores.post("/vendedores", response_model=VendedorModel)
# async def create_vendedor(vendedor: VendedorModel):
#     vendedor_dic = dict(vendedor)

#     try:
#         connection = pymysql.connect(
#         host=os.environ.get("hostDB"),
#         user=os.environ.get("userDB"),
#         password=os.environ.get("passwordDB"),
#         database=os.environ.get("databaseDB"),
#         cursorclass=pymysql.cursors.DictCursor)

#         with connection.cursor() as cursor:
#             print('evento')
#             print(vendedor_dic)
#             nombre = vendedor_dic['nombre']
#             dni = vendedor_dic['dni']
#             direccion = vendedor_dic['direccion']
#             municipio = vendedor_dic['municipio']
#             provincia = vendedor_dic['provincia'] 
#             email = vendedor_dic['email'] 
#             telefono = vendedor_dic['telefono'] 
#             fechaNacimiento = vendedor_dic['fechaNacimiento']
#             estadoCivil = vendedor_dic['estadoCivil'] 
#             fechaAlta = vendedor_dic['fechaAlta'] 
#             finalizado = vendedor_dic['finalizado']
            
            
#             query = f"INSERT INTO avap.vendedores (nombre, dni, direccion, municipio, provincia, email, telefono, fechaNacimiento, estadoCivil, fechaAlta, finalizado) VALUES ('{nombre}', '{dni}', '{direccion}', '{municipio}', '{provincia}', '{email}', '{telefono}', '{fechaNacimiento}', '{estadoCivil}', '{fechaAlta}', {finalizado});"
#             print('query insert', query)
#             cursor.execute(query)
#             connection.commit()
#             idNewvendedor = cursor.lastrowid

#             msn = f'Se ha creado un nuevo vendedor con id {idNewvendedor}'

#             response = {
#                 "headers": {
#                 'Access-Control-Allow-Origin': '*',
#                 'Access-Control-Allow-Credentials': True
#                 },
#                 "statusCode": 200,
#                 'body': json.dumps({"status":"suscess","results":msn})
#                 }
#             return response
            
#     finally:
#         cursor.close()
#         connection.close()
    
    

# Servicio para devolver vendedor por ID - GET
# @vendedores.get("/vendedores/{id}", dependencies=[Depends(JWTBearer())], tags=["vendedores"])
# async def get_vendedor(id:str):
#     try:
#         connection = pymysql.connect(
#         host=os.environ.get("hostDB"),
#         user=os.environ.get("userDB"),
#         password=os.environ.get("passwordDB"),
#         database=os.environ.get("databaseDB"),
#         cursorclass=pymysql.cursors.DictCursor)

#         with connection.cursor() as cursor:
            
#             query = f"SELECT * FROM avap.vendedores WHERE id = {id}"
#             cursor.execute(query)
#             db = cursor.fetchone()
#             print("Resultados de db: ", db)

#             response = {
#                 "headers": {
#                 'Access-Control-Allow-Origin': '*',
#                 'Access-Control-Allow-Credentials': True
#                 },
#                 "statusCode": 200,
#                 'body': json.dumps(db)
#                 }
#             return db
#     finally:
#         cursor.close()
#         connection.close()

# Servicio para borrar un vendedor por ID - DELETE
# @vendedores.delete("/vendedores/{id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())], tags=["vendedores"])
# def delete_vendedor(id:str):
#     found =  db_vendedores.find_one_and_delete({"_id": ObjectId(id)})
#     if not found:
#         return {"error":"No se ha borrado el vendedor"}

# Servicio para actualizar vendedor por ID - GET
# @vendedores.put("/vendedores/{id}", dependencies=[Depends(JWTBearer())], tags=["vendedores"])
# @vendedores.put("/vendedores/{id}", dependencies=[Depends(JWTBearer())], tags=["vendedores"])
# async def up_vendedor(id:str, vendedor:VendedorModel):
#     req = {k: v for k, v in vendedor.dict().items() if v is not None}
#     db_vendedores.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(req)})
#     return vendedorEntity( db_vendedores.find_one({"_id": ObjectId(id)}))

# Servicio para finalizar vendedor por ID - GET
# @vendedores.patch("/vendedores/{id}", dependencies=[Depends(JWTBearer())], tags=["vendedores"])
# @vendedores.patch("/vendedores/{id}", tags=["vendedores"])
# async def finalizar_vendedor(id:str, vendedorFin:VendedorModel):
#     req = {k: v for k, v in vendedorFin.dict().items() if v is not None}
#     db_vendedores.find_one_and_update({"_id": ObjectId(id)},{"$set":req})
#     return vendedorEntity( db_vendedores.find_one({"_id": ObjectId(id)}))

