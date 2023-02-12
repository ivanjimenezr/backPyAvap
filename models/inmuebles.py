from pydantic import BaseModel
from typing import Optional


class InmuebleModel(BaseModel):
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