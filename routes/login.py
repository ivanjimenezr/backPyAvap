from fastapi import APIRouter,status, Depends,Request
from fastapi.responses import FileResponse
from db.client import db_usuarios
# from schemas.usuarios import usuarioEntity, usuariosEntity
# from models.usuarios import UsuarioModel
from models.jwt import JWT
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# from starlette.responses import FileResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException


from models.usuarios import PostSchema, UserSchema, UserLoginSchema
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

usuarios = APIRouter()

# deta = Deta() 

# db = deta.Base('inmuebles') #Nombrepara la bbdd

# app = FastAPI()

# @AuthJWT.load_config
# def get_config():
#     return JWT()

# @usuarios.exception_handler(AuthJWTException)
# def authjwt_exception_handler(request: Request, exc: AuthJWTException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"detail": exc.message}
#     )

# @usuarios.post('/login')
# def login(user: UsuarioModel, Authorize: AuthJWT = Depends()):
#     #user.username
#     #user.password
#     # this is the part where we will check the user credentials with our database record
#     #but since we are not going to use any db, straight away we will just create the token and send it back
#     # subject identifier for who this token is for example id or username from database
#     access_token = Authorize.create_access_token(subject=user.email)
#     return {"access_token": access_token}