from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(id=UUID("932c6e5e-e1e4-4c34-9529-b0405a46dbd7"), 
         first_name="Ana", 
         last_name="Maria", 
         email="am@gmail.com", 
         role=[Role.role_1]
    ),
    User(id=UUID("f58ca3e3-f74d-462d-b7ed-f0e3191590b2"), 
         first_name="Isadora", 
         last_name="Bagatini", 
         email="ib@gmail.com", 
         role=[Role.role_2]
    ),
    User(id=UUID("ac08215d-47b6-4712-9aae-e3f2faa47ae9"), 
         first_name="Maria", 
         last_name="Souza", 
         email="ms@gmail.com", 
         role=[Role.role_3]
    )
]

@app.get("/")
async def root():
    return{"message": "Olá, WoMakers!"}

@app.get("/api/users")
async def get_users():
    return db

@app.get("/api/users/{id}")
async def get_user(id:UUID):
    for user in db:
        if user.id == id:
            return user
    return{"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return{"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404,
            detail=f"Usuário com o id {id} não encontrado!"
        )