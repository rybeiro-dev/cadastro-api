from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List, Type

from sqlalchemy.orm import Session
from databases.dependencies import get_db
from usuarios.models.usuario_model import Usuario

router = APIRouter()


class UserResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        orm_mode = True


class UserRequest(BaseModel):
    nome: str
    email: str


@router.get("/usuarios", response_model=List[UserResponse])
def index(db: Session = Depends(get_db)) -> List[UserResponse]:
    return db.query(Usuario).all()


@router.post("/usuarios", response_model=UserResponse, status_code=201)
def create(user: UserRequest, db: Session = Depends(get_db)) -> UserResponse:

    new_users = Usuario(
        **user.dict()
    )

    db.add(new_users)
    db.commit()
    db.refresh(new_users)

    return new_users
