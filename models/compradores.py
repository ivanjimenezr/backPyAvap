from pydantic import BaseModel
from typing import Optional


class CompradorModel(BaseModel):
    nombre: Optional[str]
    dni: Optional[str]
    direccion: Optional[str]
    municipio: Optional[str]
    provincia: Optional[str]
    email: Optional[str]
    telefono: Optional[str]
    fechaNacimiento: Optional[str]
    estadoCivil: Optional[str]
    fechaAlta: Optional[str]
    finalizado: Optional[int]