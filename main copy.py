from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from deta import Deta

# Levantar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# DETA INSTRUCTIONS
# deta visor open //para abrir la consola
# deta watch // deploy automaticamente los cambios
# deta --help

deta = Deta() 

db = deta.Base('inmuebles') #Nombrepara la bbdd

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Inmueble(BaseModel):
    tipologia: str
    provincia: str
    municipio: str
    direccion: str
    refCatastral: str
    superficie: str
    descripNotaSimple: str
    inscripcionRegistro: str
    cru: str
    precio: str
    finalizado: int
    llaves: int
    fechaAlta: str

class InmuebleUpdate(BaseModel): # Clase para el update
    tipologia: str = None
    provincia: str = None
    municipio: str = None
    direccion: str = None
    refCatastral: str = None
    superficie: str = None
    descripNotaSimple: str = None
    inscripcionRegistro: str = None
    cru: str = None
    precio: str = None
    finalizado: int = None
    llaves: int = None
    fechaAlta: str = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Serviciopara crear inmueble - POST
@app.post("/inmueble", status_code=201)
def create_inmueble(inmueble: Inmueble):
    u = db.put(inmueble.dict())
    return u

# Servicio para devolver inmueble por ID - GET
@app.get("/inmueble/{id}")
def get_inmueble(id):
    inmueble = db.get(id)
    if inmueble: # Si encuentra inmueble
        return inmueble
    else: # Si no lo encuentra
        return JSONResponse({"message":"Inmueble not found"}, status_code=404)

#Servicio para devolver todos los registros - GET
@app.get("/inmuebles/")
def get_inmuebles():
    inmueble = db.fetch()
    json_compatible_item_data = jsonable_encoder(inmueble)
    return  JSONResponse(content=json_compatible_item_data['_items'])
 
# Servicio para UPDATE inmueble por ID - PATCH
@app.patch("/inmueble/{uid}")
def update_inmueble(uid: str, uu: InmuebleUpdate):
    updates = {k:v for k,v in uu.dict().items() if v is not None}
    try:
        db.update(updates,uid)
        return db.get(uid)
    except Exception:
        return JSONResponse({"message":"Inmueble not found"}, status_code=404)

# Servicio para borrar un inmueble por ID - DELETE
@app.delete("/inmueble/{id}")
def delete_inmueble(id:str):
    try:
        db.delete(id)
        return JSONResponse({"message":"Inmueble deleted"}, status_code=200)
    except Exception:
        return JSONResponse({"message":"Inmueble not found"}, status_code=404)
