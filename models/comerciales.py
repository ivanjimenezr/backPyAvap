from pydantic import BaseModel
from typing import Optional,List


class ComercialesModel(BaseModel):
    nombre: Optional[str]

    # vendedores: Optional[list]


# class InmuebleUpdate(BaseModel): # Clase para el update
#     tipologia: str = None
#     provincia: str = None
#     municipio: str = None
#     direccion: str = None
#     refCatastral: str = None
#     superficie: str = None
#     descripNotaSimple: str = None
#     inscripcionRegistro: str = None
#     cru: str = None
#     precio: str = None
#     finalizado: str = None
#     llaves: str = None
    # fechaAlta: str = None