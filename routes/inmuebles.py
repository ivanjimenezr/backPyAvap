from fastapi import APIRouter,status, Response,BackgroundTasks, Depends
from fastapi.responses import FileResponse
from db.client import db_inmuebles, db_asociaciones
from schemas.inmuebles import inmuebleEntity, inmueblesEntity
from schemas.asociaciones import asociacionEntity,asociacionesEntity
from models.inmuebles import InmuebleModel
from models.asociaciones import AsociacioneModels
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

import db.ConnToMysql as dataBase
# from starlette.responses import FileResponse

# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter, A4

# from reportlab.lib.styles import ParagraphStyle
# from reportlab.lib.styles import getSampleStyleSheet

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

inmuebles = APIRouter()

# deta = Deta() 

# db = deta.Base('inmuebles') #Nombrepara la bbdd

# app = FastAPI()


# try:

    # connection = pymysql.connect(
    #         host=os.environ.get("hostDB"),
    #         user=os.environ.get("userDB"),
    #         password=os.environ.get("passwordDB"),
    #         database=os.environ.get("databaseDB"),
    #         cursorclass=pymysql.cursors.DictCursor)

    # with connection.cursor() as cursor:

    

#Servicio para devolver todos los inmuebles - GET
# @inmuebles.get("/inmuebles", dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
@inmuebles.get("/inmuebles", tags=["inmuebles"])
async def list_inmuebles():
    # try:
    allInmu = dataBase.get_all_inmuebles()
    
    # connection = pymysql.connect(
    # host=os.environ.get("hostDB"),
    # user=os.environ.get("userDB"),
    # password=os.environ.get("passwordDB"),
    # database=os.environ.get("databaseDB"),
    # cursorclass=pymysql.cursors.DictCursor)

    # with connection.cursor() as cursor:
        
    #     query = "SELECT * FROM avap.inmuebles"
    #     cursor.execute(query)
    #     db = cursor.fetchall()
        # print("Resultados de db: ", db)

    allInmuebles = []
    for nn in allInmu:
        print('kk',nn)
        idInmueble = nn[0]
        print('idInmueble: ', idInmueble)
        # query2 = f"SELECT * FROM avap.vendedores where id IN (SELECT idVendedor FROM avap.asociaciones WHERE idInmueble = {idInmueble});"
        # cursor.execute(query2)
        # dbVendedores = cursor.fetchall()
        dbVendedores = dataBase.get_vendedor_id_inmuebles(idInmueble)
        # if dbVendedores:
        #     nn['vendedores'] = dbVendedores
        # else:
        #     nn['vendedores'] = []
        # allInmuebles.append(nn)
        
        # print('llll',allInmuebles)


        response = {
            "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
            },
            "statusCode": 200,
            'body': json.dumps(allInmu)
            }
        return allInmu
    # finally:
    #     cursor.close()
    #     connection.close()
    # return  inmueblesEntity(db_inmuebles.find())


    #Servicio para devolver todos los registros - GET


# Servicio para devolver inmueble por ID - GET
# @inmuebles.get("/inmuebles", dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
@inmuebles.get("/inmuebles/{id}", tags=["inmuebles"])
async def list_inmuebles(id:int):
    try:
        connection = pymysql.connect(
        host=os.environ.get("hostDB"),
        user=os.environ.get("userDB"),
        password=os.environ.get("passwordDB"),
        database=os.environ.get("databaseDB"),
        cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            
            query = f"SELECT * FROM avap.inmuebles where id = {id}"
            cursor.execute(query)
            db = cursor.fetchone()
            print("Resultados de db: ", db)


            
            
            print('idInmueble: ', id)
            query2 = f"SELECT * FROM avap.vendedores where id IN (SELECT idVendedor FROM avap.asociaciones WHERE idInmueble = {id});"
            cursor.execute(query2)
            dbVendedores = cursor.fetchall()
            if dbVendedores:
                db['vendedores'] = dbVendedores
            else:
                db['vendedores'] = []
            
            # print('llll',allInmuebles)


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

    


# Servicio para crear inmueble - POST
# @inmuebles.post("/inmuebles", response_model=InmuebleModel, dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
@inmuebles.post("/inmuebles")
async def create_inmueble(inmueble:InmuebleModel):
    inmueble = dict(inmueble)
    print('inmueble', inmueble)
    try:
        connection = pymysql.connect(
        host=os.environ.get("hostDB"),
        user=os.environ.get("userDB"),
        password=os.environ.get("passwordDB"),
        database=os.environ.get("databaseDB"),
        cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            print('evento')
            print(inmueble)
            print('eventotipo')
            print(type(inmueble))
            tipologia = inmueble['tipologia']
            provincia = inmueble['provincia']
            municipio = inmueble['municipio']
            direccion = inmueble['direccion']
            refCatastral = inmueble['refCatastral'] 
            superficie = inmueble['superficie'] 
            descripNotaSimple = inmueble['descripNotaSimple'] 
            inscripcionRegistro = inmueble['inscripcionRegistro']
            cru = inmueble['cru'] 
            precio = inmueble['precio'] 
            finalizado = inmueble['finalizado']
            llaves = inmueble['llaves']
            fechaAlta= inmueble['fechaAlta']
            comisionVen= inmueble['comisionVen']
            comisionCom= inmueble['comisionCom']
            observaciones= inmueble['observaciones']
            comercial= inmueble['comercial']
            dormitorios= inmueble['dormitorios']
            banos= inmueble['banos']
            exterior= inmueble['exterior']
            operacion= inmueble['operacion']
            cee= inmueble['cee']
            cee= inmueble['cee']
            descripcion= inmueble['descripcion']
            ascensor= inmueble['ascensor']
            
            query = f"INSERT INTO avap.inmuebles (tipologia, provincia, municipio, direccion, refCatastral, superficie, descripNotaSimple, inscripcionRegistro, cru, precio, finalizado, llaves, fechaAlta, comisionVen,comisionCom,observaciones,comercial,dormitorios,banos,exterior,operacion,cee,descripcion,ascensor) VALUES ('{tipologia}', '{provincia}', '{municipio}', '{direccion}', '{refCatastral}', '{superficie}', '{descripNotaSimple}', '{inscripcionRegistro}', '{cru}', '{precio}', '{finalizado}', '{llaves}', '{fechaAlta}', '{comisionVen}', '{comisionCom}', '{observaciones}', '{comercial}', '{dormitorios}', '{banos}', '{exterior}', '{operacion}', '{cee}', '{descripcion}', '{ascensor}');"
            print('query insert', query)
            cursor.execute(query)
            connection.commit()
            idNewInmueble = cursor.lastrowid

            msn = f'Se ha creado un inmueble con id {idNewInmueble}'

            response = {
                "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
                },
                "statusCode": 200,
                'body': json.dumps({"status":"suscess","results":msn})
                }
            return response
        
    finally:
        cursor.close()
        connection.close()
    

# Servicio para devolver inmueble por ID - GET
# @inmuebles.get("/inmuebles/{id}", dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
# async def get_inmueble(id:str):
#     return inmuebleEntity( db_inmuebles.find_one({"_id": ObjectId(id)}))

# Servicio para borrar un inmueble por ID - DELETE
# @inmuebles.delete("/inmuebles/{id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
# def delete_inmueble(id:str):
#     found =  db_inmuebles.find_one_and_delete({"_id": ObjectId(id)})
#     if not found:
#         return {"error":"No se ha borrado el inmueble"}

# Servicio para actualizar inmueble por ID - GET
# @inmuebles.put("/inmuebles/{id}", dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
# @inmuebles.put("/inmuebles/{id}")
# async def up_inmueble(id:str, inmueble:InmuebleModel):
#     print('inmuebleUP: ', inmueble)
#     req = {k: v for k, v in inmueble.dict().items() if v is not None}
#     db_inmuebles.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(req)})
#     return inmuebleEntity( db_inmuebles.find_one({"_id": ObjectId(id)}))

# Servicio para actualizar inmueble - POST
# @inmuebles.post("/inmuebles{id}", response_model=InmuebleModel, dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
@inmuebles.post("/inmuebles/{id}")
async def up_inmueble(id:str, inmueble:InmuebleModel):
    inmueble = dict(inmueble)
    print('inmueble', inmueble)
    try:
        connection = pymysql.connect(
        host=os.environ.get("hostDB"),
        user=os.environ.get("userDB"),
        password=os.environ.get("passwordDB"),
        database=os.environ.get("databaseDB"),
        cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            print('evento')
            print(inmueble)
            print('eventotipo')
            print(type(inmueble))
            tipologia = inmueble['tipologia']
            provincia = inmueble['provincia']
            municipio = inmueble['municipio']
            direccion = inmueble['direccion']
            refCatastral = inmueble['refCatastral'] 
            superficie = inmueble['superficie'] 
            descripNotaSimple = inmueble['descripNotaSimple'] 
            inscripcionRegistro = inmueble['inscripcionRegistro']
            cru = inmueble['cru'] 
            precio = inmueble['precio'] 
            finalizado = inmueble['finalizado']
            llaves = inmueble['llaves']
            fechaAlta= inmueble['fechaAlta']
            comisionVen= inmueble['comisionVen']
            comisionCom= inmueble['comisionCom']
            observaciones= inmueble['observaciones']
            comercial= inmueble['comercial']
            dormitorios= inmueble['dormitorios']
            banos= inmueble['banos']
            exterior= inmueble['exterior']
            operacion= inmueble['operacion']
            cee= inmueble['cee']
            descripcion= inmueble['descripcion']
            ascensor= inmueble['ascensor']
            
            query = f"UPDATE avap.inmuebles SET tipologia = '{tipologia}', provincia = '{provincia}', municipio = '{municipio}', direccion = '{direccion}', refCatastral = '{refCatastral}', superficie = '{superficie}', descripNotaSimple = '{descripNotaSimple}', inscripcionRegistro = '{inscripcionRegistro}', cru = '{cru}', precio = '{precio}', finalizado = {finalizado}, llaves = {llaves}, fechaAlta = '{fechaAlta}', comisionVen = '{comisionVen}', comisionCom = '{comisionCom}', observaciones = '{observaciones}', comercial = '{comercial}', dormitorios = '{dormitorios}', banos = '{banos}', exterior = '{exterior}', operacion = '{operacion}', cee = '{cee}', descripcion = '{descripcion}', ascensor = '{ascensor}' WHERE id = {id};"
            print('query insert', query)
            cursor.execute(query)
            connection.commit()

            msn = f'Se ha actualizado el inmueble con id {id}'

            response = {
                "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
                },
                "statusCode": 200,
                'body': json.dumps({"status":"suscess","results":msn})
                }
            return response
        
    finally:
        cursor.close()
        connection.close()
    

# Servicio para finalizar inmueble por ID - GET
# @inmuebles.patch("/inmuebles/{id}", dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
# async def finalizar_inmueble(id:str, inmuebleFin:InmuebleModel):
#     req = {k: v for k, v in inmuebleFin.dict().items() if v is not None}
#     db_inmuebles.find_one_and_update({"_id": ObjectId(id)},{"$set":req})
#     return inmuebleEntity( db_inmuebles.find_one({"_id": ObjectId(id)}))

# Servicio para finalizar inmueble - patch
# @inmuebles.patch("/inmuebles{id}", response_model=InmuebleModel, dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
@inmuebles.patch("/inmuebles/{id}")
async def finalizar_inmueble(id:str, inmuebleFin:InmuebleModel):
    try:
        connection = pymysql.connect(
        host=os.environ.get("hostDB"),
        user=os.environ.get("userDB"),
        password=os.environ.get("passwordDB"),
        database=os.environ.get("databaseDB"),
        cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            print('evento PATCH')
            print(id)
            print(inmuebleFin)
            inmuebleFin = dict(inmuebleFin)
            estadoFin = inmuebleFin['finalizado']

            query = f"UPDATE avap.inmuebles SET finalizado = {estadoFin} WHERE id = {id};"
            print('query insert', query)
            cursor.execute(query)
            connection.commit()

            msn = f'Se ha cambiado el estado de finalizado el inmueble con id {id}'

            response = {
                "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
                },
                "statusCode": 200,
                'body': json.dumps({"status":"suscess","results":msn})
                }
            return response
        
    finally:
        cursor.close()
        connection.close()


# Servicio para asociar vendedor a inmueble - patch
# @inmuebles.post("/inmuebles{id}", response_model=InmuebleModel, dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
@inmuebles.post("/asociaVendedor/{id}")
async def createAsociaVendedor(id,asociaVendedor:AsociacioneModels):
    asociaVendedor_dic = dict(asociaVendedor)
    hh = asociaVendedor_dic['idVendedor']

    try:
        connection = pymysql.connect(
        host=os.environ.get("hostDB"),
        user=os.environ.get("userDB"),
        password=os.environ.get("passwordDB"),
        database=os.environ.get("databaseDB"),
        cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            for vendedor in hh:
                print(vendedor['id'])
                # Preguntamos por si la asociacion ya existe
                query = f"SELECT * FROM avap.asociaciones where idInmueble = {id} and idVendedor = {vendedor['id']}"
                cursor.execute(query)
                found = cursor.fetchone()
                # found = db_asociaciones.find_one({"idInmueble":id,"idVendedor":vendedor['id']})
                if not found:
                    print('no existe asocio')
                    query = f"INSERT INTO avap.asociaciones (idInmueble, idVendedor) VALUES ({id}, {vendedor['id']});"
                    print('query insert', query)
                    cursor.execute(query)
                    connection.commit()
                    # db_asociaciones.insert_one({"idInmueble":id,"idVendedor":vendedor['id']})
                    msn = 'No esta asociado, creo la asociación'
                else:
                    print('Ya existe la asociacion')
                    print(found)
                    msn = 'Ya existe la asociacion'
            return  msn
            
            

            msn = f'Se ha actualizado el inmueble con id {id}'

            response = {
                "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
                },
                "statusCode": 200,
                'body': json.dumps({"status":"suscess","results":msn})
                }
            return response
        
    finally:
        cursor.close()
        connection.close()

    


# Servicio para asociar vendedor a inmueble
# @inmuebles.post("/asociaVendedor/{id}", dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
# @inmuebles.post("/asociaVendedor/{id}")
# async def createAsociaVendedor(id,asociaVendedor:AsociacioneModels):
#     asociaVendedor_dic = dict(asociaVendedor)
#     hh = asociaVendedor_dic['idVendedor']
#     for vendedor in hh:
#         print(vendedor['id'])
#         # Preguntamos por si la asociacion ya existe
#         found = db_asociaciones.find_one({"idInmueble":id,"idVendedor":vendedor['id']})
#         if not found:
#             print('no existe asocio')
#             db_asociaciones.insert_one({"idInmueble":id,"idVendedor":vendedor['id']})
#             msn = 'No esta asociado, creo la asociación'
#         else:
#             print('Ya existe la asociacion')
#             print(found)
#             msn = 'Ya existe la asociacion'
#     return  msn

# Servicio para devolver vendedores por inmueble
# @inmuebles.get("/asociaVendedor/{id}", dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
# async def getAsociaVendedor(id:str):
#     return   asociacionesEntity(db_asociaciones.find({"idInmueble": id}, {"idInmueble": 1,"idVendedor": 1}))



# finally:
    # cursor.close()
    # connection.close()
    # print("MySQL connection is closed")


# Servicio para contrato arras
# @inmuebles.get("/inmuebles/arras/{id}", dependencies=[Depends(JWTBearer())], tags=["inmuebles"])
# async def get_inmueble(id:str,background_tasks: BackgroundTasks):
#     inmueble = inmuebleEntity( db_inmuebles.find_one({"_id": ObjectId(id)}))
    
#     id = inmueble['id']
#     tipologia=inmueble['tipologia']
#     provincia=inmueble['provincia']
#     municipio=inmueble['municipio']
    
#     print('id: ', id)
#     print('tipologia: ', tipologia)

#     buf = io.BytesIO()

#     c = canvas.Canvas(buf, pagesize=A4)
#     text = c.beginText(50, 350)
#     text.setFont("Times-Roman", 12)
#     # El método textLines() soporta el carácter de salto de línea.
#     text.textLines("¡Hola, mundo!\n¡Desde ReportLab y Python!")
#     c.drawText(text)
#     c.drawString(50, 300, tipologia)
#     c.drawString(50, 200, f'El contrato presente del señor {provincia} con domicilio en {provincia} esto si es bueno')
#     c.drawString(50, 150, municipio)
#     c.drawString(50, 100, municipio)
#     # c.drawImage("PNG.gif", 150,300 )
#     # c.drawString(50, 50, create_at)
#     c.save()
#     buf.seek(0)
#     # buf.close
#     background_tasks.add_task(buf.close)
#     headers = {'Content-Disposition': 'inline; filename="out.pdf"'}
#     return Response(buf, headers=headers, media_type='application/pdf')
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


