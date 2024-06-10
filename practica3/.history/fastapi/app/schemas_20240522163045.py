from typing import Dict
from pydantic import BaseModel,Field


class User(BaseModel):
    __tablename__ = "users"
    id: int = Field(..., description="id del producto")
    name: str = Field(..., description="nombre del producto")
    emails: str = Field(..., description="email del usuario")

class ItemCreate(User):
    pass

class Item(User):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

    class Config:
        orm_mode = True