from typing import Dict,Field
from pydantic import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    id: int = Field(..., description="id del producto")
    name: str = Field(..., description="nombre del producto")
    emails: str = Field(..., description="email del usuario")