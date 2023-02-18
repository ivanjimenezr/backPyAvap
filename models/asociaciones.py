from pydantic import BaseModel
from typing import Optional


class AsociacioneModels(BaseModel):
    idInmueble: Optional[str]
    idVendedor: Optional[list]