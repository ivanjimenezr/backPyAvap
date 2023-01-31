# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480)

### MongoDB client ###

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost

# from pymongo import MongoClient
from deta import Deta

# Descomentar el db_client local o remoto correspondiente

# Base de datos local MongoDB
# db_client = MongoClient().local

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=25470

# Base de datos remota MongoDB Atlas (https://mongodb.com)
# db_client = MongoClient(
#     "mongodb+srv://chiklete:<password>@cluster0.f3k1j.mongodb.net/test"
#     # "mongodb+srv://chiklete:<password>@cluster0.f3k1j.mongodb.net/test"
    
#     )
    

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/

deta = Deta() 

db = deta.Base('inmuebles') #Nombre para la bbdd
db = deta.Base('compradores') #Nombre para la bbdd
db = deta.Base('vendedores') #Nombre para la bbdd