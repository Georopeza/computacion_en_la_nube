from typing import Dict, Tuple
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlmodel import Session, SQLModel, create_engine


app = FastAPI()

class User(SQLModel, table=True):
    id: int = Field(..., description="id del producto")
    name: str = Field(..., description="nombre del producto")
    emails: list[str]
    
sqlite_url = "sqlite:///users.db"
engine = create_engine(sqlite_url)

engine: Dict[int, list] = {}

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_book(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()    

new_book = User(title="1984", author="George Orwell", year=1949)
create_book(new_book)       

# retorno de msg de prueba 
@app.get("/")
async def welcome():
    return {"message":"Computacion en la nube prueba"}

# prueba de status 
@app.get("/status/")
def status():
    return {"message": "Pong"}

# lista de objetos 
@app.get("/directories/")
def listado_objetos():
    return engine

# Insertar nombre e email del usuario
@app.post("/directories/")
def set_product(user: User) -> User:
    print("Ingrese el nombre")
    new_name = input()
    print("Ingrese el email")
    new_email = input()
    user = new_name,new_email
    engine.append(user)
    return user

# retorna una db por el id del usuario
@app.get("/directories/{id}")
def find_by_id(id: int)-> User | None:
    user_tuple = engine.get(id)
    
    if user_tuple:       
        return  User(id=id, name=user_tuple[id], emails=user_tuple[id])
    return None

# nuevo email y nombre para el usuario
@app.put("/directories/{id}")
def edit_by_id(id: int, user:User)-> User | None:
    print("Ingrese el nuevo nombre")
    new_name = input()
    print("Ingrese el nuevo email")
    new_email = input()
    user = new_name,new_email
    user_tuple = engine.get(id)
    
    if user_tuple:
        engine[user.id] = user
        return user
    return None

# nuevo email y nombre para el usuario
@app.patch("/directories/{id}")
def edit_temp_by_id(id: int, user:User)-> User | None:
    print("Ingrese el nuevo nombre")
    new_name = input()
    print("Ingrese el nuevo email")
    new_email = input()
    user = new_name,new_email
    user_tuple = engine.get(id)
    
    if user_tuple:
        engine[user.id] = user
        return user
    return None

@app.delete("/directories/{id}")
def delete_by_id(id: int):
    del engine[id]
    return None