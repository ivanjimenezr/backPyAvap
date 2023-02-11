# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480)

### MongoDB client ###

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost

from pymongo import MongoClient,mongo_client 
from dotenv import dotenv_values


config = dotenv_values('.env')
# Descomentar el db_client local o remoto correspondiente

# Base de datos local MongoDB
db_client = mongo_client.MongoClient(config['ATLAS_URI'])
print('Connected to MongoDB...')

db = db_client[config['DB_NAME']] 

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=25470

# Base de datos remota MongoDB Atlas (https://mongodb.com)
# db_client = MongoClient(
#     "mongodb+srv://chiklete:<password>@cluster0.f3k1j.mongodb.net/test"
#     # "mongodb+srv://chiklete:<password>@cluster0.f3k1j.mongodb.net/test"
    
#     )
    

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/

# deta = Deta() 

db_inmuebles = db.inmuebles #Nombre para la bbdd
db_compradores = db.compradore #Nombre para la bbdd
db_vendedores = db.vendedores #Nombre para la bbdd