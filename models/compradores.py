from pydantic import BaseModel


class Comprador(BaseModel):
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

class CompradorUpdate(BaseModel): # Clase para el update
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