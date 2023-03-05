from fastapi import APIRouter,status, Response,BackgroundTasks,Depends
from fastapi.responses import FileResponse
from db.client import db_vendedores
from schemas.vendedores import vendedorEntity, vendedoresEntity
from models.vendedores import VendedorModel
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
# from starlette.responses import FileResponse

from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer

import pymysql.cursors
from dotenv import dotenv_values,load_dotenv
import os
import json

load_dotenv('.env') 
# deta --help 

comerciales = APIRouter()

#Servicio para devolver todos los registros - GET
@comerciales.get("/comerciales")
async def list_comerciales():
    try:
        connection = pymysql.connect(
        host=os.environ.get("hostDB"),
        user=os.environ.get("userDB"),
        password=os.environ.get("passwordDB"),
        database=os.environ.get("databaseDB"),
        cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            
            query = "SELECT * FROM avap.comerciales"
            cursor.execute(query)
            db = cursor.fetchall()
            print("Resultados de db: ", db)

            response = {
                "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
                },
                "statusCode": 200,
                'body': json.dumps(db)
                }
            return db
    finally:
        cursor.close()
        connection.close()
    # return  vendedoresEntity(db_vendedores.find())


