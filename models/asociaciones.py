from pydantic import BaseModel
from typing import Optional


class AsociacioneModels(BaseModel):
    idInmueble: Optional[str]
    idVendedor: Optional[list]

class AsociacioneCompraModels(BaseModel):
    idInmueble: Optional[str]
    idComprador: Optional[list]