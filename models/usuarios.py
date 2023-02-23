from pydantic import BaseModel
from typing import Optional


class UsuarioModel(BaseModel):
    email: str
    password: str
    