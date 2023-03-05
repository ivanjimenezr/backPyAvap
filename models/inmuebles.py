from pydantic import BaseModel
from typing import Optional,List


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
    dormitorios: Optional[str]
    banos: Optional[str]
    exterior: Optional[str]
    comisionVen: Optional[str]
    comercial: Optional[str]
    observaciones: Optional[str]
    comisionCom: Optional[str]
    operacion: Optional[str]
    cee: Optional[str]
    descripcion: Optional[str]
    ascensor: Optional[str]

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