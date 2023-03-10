from fastapi import APIRouter,status, Response,BackgroundTasks
from fastapi.responses import FileResponse
from db.client import db_inmuebles
from schemas.inmuebles import inmuebleEntity, inmueblesEntity
from models.inmuebles import InmuebleModel
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

inmuebles = APIRouter()

# deta = Deta() 

# db = deta.Base('inmuebles') #Nombrepara la bbdd

# app = FastAPI()




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
    req = {k: v for k, v in inmueble.dict().items() if v is not None}
    db_inmuebles.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(req)})
    return inmuebleEntity( db_inmuebles.find_one({"_id": ObjectId(id)}))

# Servicio para finalizar inmueble por ID - GET
@inmuebles.patch("/inmuebles/{id}")
async def finalizar_inmueble(id:str, inmuebleFin:InmuebleModel):
    req = {k: v for k, v in inmuebleFin.dict().items() if v is not None}
    db_inmuebles.find_one_and_update({"_id": ObjectId(id)},{"$set":req})
    return inmuebleEntity( db_inmuebles.find_one({"_id": ObjectId(id)}))

# Servicio para contrato arras
@inmuebles.get("/inmuebles/arras/{id}")
async def get_inmueble(id:str,background_tasks: BackgroundTasks):
    inmueble = inmuebleEntity( db_inmuebles.find_one({"_id": ObjectId(id)}))
    
    id = inmueble['id']
    tipologia=inmueble['tipologia']
    provincia=inmueble['provincia']
    municipio=inmueble['municipio']
    
    print('id: ', id)
    print('tipologia: ', tipologia)

    buf = io.BytesIO()

    c = canvas.Canvas(buf, pagesize=A4)
    text = c.beginText(50, 350)
    text.setFont("Times-Roman", 12)
    # El método textLines() soporta el carácter de salto de línea.
    text.textLines("¡Hola, mundo!\n¡Desde ReportLab y Python!")
    c.drawText(text)
    c.drawString(50, 300, tipologia)
    c.drawString(50, 200, f'El contrato presente del señor {provincia} con domicilio en {provincia} esto si es bueno')
    c.drawString(50, 150, municipio)
    c.drawString(50, 100, municipio)
    # c.drawImage("PNG.gif", 150,300 )
    # c.drawString(50, 50, create_at)
    c.save()
    buf.seek(0)
    # buf.close
    background_tasks.add_task(buf.close)
    headers = {'Content-Disposition': 'inline; filename="out.pdf"'}
    return Response(buf, headers=headers, media_type='application/pdf')
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


