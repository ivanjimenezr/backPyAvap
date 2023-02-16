from fastapi import APIRouter,status, Response,BackgroundTasks
from fastapi.responses import FileResponse
from db.client import db_vendedores
from schemas.vendedores import vendedorEntity, vendedoresEntity
from models.vendedores import VendedorModel
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
# from starlette.responses import FileResponse

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet

import io

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
    return  vendedoresEntity(db_vendedores.find())


# Serviciopara crear vendedores - POST
@vendedores.post("/vendedores", response_model=VendedorModel)
async def create_vendedor(vendedor: VendedorModel):
    vendedor_dic = dict(vendedor)
    id = db_vendedores.insert_one(vendedor_dic).inserted_id
    new_inmueble = db_vendedores.find_one({"_id": id})
    return vendedorEntity(new_inmueble)
    

# Servicio para devolver vendedor por ID - GET
@vendedores.get("/vendedores/{id}")
async def get_vendedor(id:str):
    return vendedorEntity( db_vendedores.find_one({"_id": ObjectId(id)}))

# Servicio para borrar un vendedor por ID - DELETE
@vendedores.delete("/vendedores/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendedor(id:str):
    found =  db_vendedores.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"error":"No se ha borrado el vendedor"}

# Servicio para actualizar vendedor por ID - GET
@vendedores.put("/vendedores/{id}")
async def up_vendedor(id:str, vendedor:VendedorModel):
    req = {k: v for k, v in vendedor.dict().items() if v is not None}
    db_vendedores.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(req)})
    return vendedorEntity( db_vendedores.find_one({"_id": ObjectId(id)}))

# Servicio para finalizar vendedor por ID - GET
@vendedores.patch("/vendedores/{id}")
async def finalizar_vendedor(id:str, vendedorFin:VendedorModel):
    req = {k: v for k, v in vendedorFin.dict().items() if v is not None}
    db_vendedores.find_one_and_update({"_id": ObjectId(id)},{"$set":req})
    return vendedorEntity( db_vendedores.find_one({"_id": ObjectId(id)}))


    # headers = {'Content-Disposition': 'inline; filename="out.pdf"'}
    # pdf = buf.getvalue()
    # buf.close()
    
    
    # return inmueble, FileResponse
    # headers = {'Content-Disposition': 'attachment; filename="arras.pdf"'}
    # headers=['Content- Type','Authorization']
    # headers=['Content- Type','Authorization']
    # pdf.add('Access-Control-Allow-Origin', '*')
    # return FileResponse(buf)
    # return


# Servicio para UPDATE inmueble por ID - PATCH
# @inmuebles.patch("/{uid}")
# def update_inmueble(uid: str, uu: InmuebleUpdate):
#     updates = {k:v for k,v in uu.dict().items() if v is not None}
#     try:
#         client.db.update(updates,uid)
#         return client.db_inmuebles.get(uid)
#     except Exception:
#         return JSONResponse({"message":"Inmueble not found"}, status_code=404)


