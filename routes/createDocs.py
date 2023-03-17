from fastapi import APIRouter,status, Response,BackgroundTasks, Depends
from fastapi.responses import FileResponse

from docx import Document
from docx.shared import Inches

# from db.client import db_inmuebles, db_asociaciones
# from schemas.inmuebles import inmuebleEntity, inmueblesEntity
# from schemas.asociaciones import asociacionEntity,asociacionesEntity
# from models.inmuebles import InmuebleModel
# from models.asociaciones import AsociacioneModels
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
# from starlette.responses import FileResponse,StreamingResponse

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
import io
import ftplib

import db.ConnToMysql as dataBase

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

docs = APIRouter()

# deta = Deta() 

# db = deta.Base('inmuebles') #Nombrepara la bbdd

# app = FastAPI()





@docs.get("/arras/{id}")
async def docs_arras(id:int):
    db = dataBase.get_inmueble_id(id)
    #try:
        #connection = pymysql.connect(
        #host=os.environ.get("hostDB"),
        #user=os.environ.get("userDB"),
        #password=os.environ.get("passwordDB"),
        #database=os.environ.get("databaseDB"),
        #cursorclass=pymysql.cursors.DictCursor)

        #with connection.cursor() as cursor:
            
            #query = f"SELECT * FROM avap.inmuebles WHERE id = {id}"
            #cursor.execute(query)
            #db = cursor.fetchone()
            #print("Resultados de db: ", db)
    tipologia = db['tipologia']
    document = Document()

    document.add_heading('Documento de Arras', 0)

    p = document.add_paragraph(f'A plain paragraph having some {tipologia}')
    p.add_run('bold').bold = True
    p.add_run(' and some ')
    p.add_run('italic.').italic = True

    document.add_heading('Heading, level 1', level=1)
    document.add_paragraph('Intense quote', style='Intense Quote')

    document.add_paragraph('first item in unordered list', style='List Bullet')
    document.add_paragraph('first item in ordered list', style='List Number')

            # document.add_picture('monty-truth.png', width=Inches(1.25))

    records = (
        (3, '101', 'Spam'),
        (7, '422', 'Eggs'),
        (4, '631', 'Spam, spam, eggs, and spam'))

    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'
    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc

    document.add_page_break()

    #document.save('arras.docx')
    # threFile = document.save('demo.docx')

    bio = io.BytesIO()
    document.save(bio)  # save to memory stream
    bio.seek(0)  # rewind the stream
            

            ### FTPPPPPPP --------------------------------------------

    # domain name or server ip:
    ftpHost = os.environ.get("ftp_host")
    ftpPort = 21
    ftpUname = os.environ.get("ftp_user")
    ftpPass = os.environ.get("ftp_password")

    ftp = ftplib.FTP(timeout=30)
    ftp.connect(ftpHost, ftpPort)
    ftp.login(ftpUname, ftpPass)

    # fnames = ftp.nlst()

    ftp.cwd("httpdocs/files")

    localFilePath = 'arras.docx'

    with open(localFilePath, 'rb') as file:
        retCode =ftp.storbinary('STOR arras.docx', file, blocksize=1024*1024)

        ftp.quit()

        if retCode.startswith('256'):
            print('upload success')
        else:
            print('upload not success...')

        print('Ejecucion completa')

            ### FTPPPPPPP --------------------------------------------
            
        return f'http://panel.acapagencia.com/files/{localFilePath}'
        # return FileResponse(bio, media_type='application/octet-stream')
        # return StreamingResponse(bio.read(), media_type='application/octet-stream')


        