from pydantic import BaseModel
from typing import Optional


class JWT(BaseModel):
    authjwt_secret_key: str = "my_jwt_secret"
    