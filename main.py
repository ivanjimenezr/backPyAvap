from fastapi import FastAPI,Body,Depends
from routes.inmuebles import inmuebles
from routes.vendedores import vendedores
from routes.compradores import compradores
from routes.login import usuarios
from fastapi.middleware.cors import CORSMiddleware

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet

from models.usuarios import PostSchema, UserSchema, UserLoginSchema
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer


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
app.include_router(vendedores)
app.include_router(compradores)
# app.include_router(usuarios)

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }



# @app.get("/inmuebles")
# def read_root():
#     return {"Hello": "World"}

# # Serviciopara crear inmueble - POST
# @app.post("/inmueble", status_code=201)
# def create_inmueble(inmueble: Inmueble):
#     u = db.put(inmueble.dict())
#     return u

# # Servicio para devolver inmueble por ID - GET
# @app.get("/inmueble/{id}")
# def get_inmueble(id):
#     inmueble = db.get(id)
#     if inmueble: # Si encuentra inmueble
#         return inmueble
#     else: # Si no lo encuentra
#         return JSONResponse({"message":"Inmueble not found"}, status_code=404)

# #Servicio para devolver todos los registros - GET
# @app.get("/inmuebles/")
# def get_inmuebles():
#     inmueble = db.fetch()
#     json_compatible_item_data = jsonable_encoder(inmueble)
#     return  JSONResponse(content=json_compatible_item_data['_items'])
 
# # Servicio para UPDATE inmueble por ID - PATCH
# @app.patch("/inmueble/{uid}")
# def update_inmueble(uid: str, uu: InmuebleUpdate):
#     updates = {k:v for k,v in uu.dict().items() if v is not None}
#     try:
#         db.update(updates,uid)
#         return db.get(uid)
#     except Exception:
#         return JSONResponse({"message":"Inmueble not found"}, status_code=404)

# # Servicio para borrar un inmueble por ID - DELETE
# @app.delete("/inmueble/{id}")
# def delete_inmueble(id:str):
#     try:
#         db.delete(id)
#         return JSONResponse({"message":"Inmueble deleted"}, status_code=200)
#     except Exception:
#         return JSONResponse({"message":"Inmueble not found"}, status_code=404)
