from fastapi import FastAPI,Body,Depends
from routes.inmuebles import inmuebles
# from routes.vendedores import vendedores
from routes.compradores import compradores
from routes.comerciales import comerciales
from routes.login import usuarios
from routes.createDocs import docs
from fastapi.middleware.cors import CORSMiddleware

# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter, A4

# from reportlab.lib.styles import ParagraphStyle
# from reportlab.lib.styles import getSampleStyleSheet

from models.usuarios import PostSchema, UserSchema, UserLoginSchema
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer
from bson import ObjectId
# from db.client import db_usuarios

# import pymysql
# from dotenv import dotenv_values,load_dotenv
# import os
# import json
# import db.ConnToMysql as dataBase

# load_dotenv('.env') 





# Levantar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# DETA INSTRUCTIONS
# deta visor open //para abrir la consola
# deta watch // deploy automaticamente los cambios
# deta --help

# deta = Deta() 

# db = deta.Base('inmuebles') #Nombrepara la bbdd

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = []

app.include_router(inmuebles)
# app.include(vendedores)
app.include_router(compradores)
app.include_router(comerciales)
app.include_router(docs)
# app.include_router(usuarios)

# @app.post("/user/signup", tags=["user"])
# async def create_user(user: UserSchema = Body(...)):
#     users.append(user) # replace with db call, making sure to hash the password first
#     return signJWT(user.email)

# def check_user(data: UserLoginSchema):
#     data = dict(data)
#     pd = dataBase.find_usuario(data)
#     return pd

# @app.post("/user/login", tags=["user"])
# async def user_login(user: UserLoginSchema = Body(...)):
#     if check_user(user):
#         return signJWT(user.email)
#     return {
#         "error": "Wrong login details!"
#     }
