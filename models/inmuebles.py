from pydantic import BaseModel
from typing import Optional


class InmuebleModel(BaseModel):
    tipologia: Optional[str]
    provincia: Optional[str]
    municipio: Optional[str]
    direccion: Optional[str]
    refCatastral: Optional[str]
    superficie: Optional[str]
    descripNotaSimple: Optional[str]
    inscripcionRegistro: Optional[str]
    cru: Optional[str]
    precio: Optional[str]
    finalizado: Optional[int]
    llaves: Optional[int]
    fechaAlta: Optional[str]

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