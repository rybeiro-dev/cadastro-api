from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class UserResponse(BaseModel):
    id: int
    nome: str
    email: str


class UserRequest(BaseModel):
    nome: str
    email: str


@router.get("/usuarios", response_model=List[UserResponse])
def index():
    return [
        UserResponse(
            id=1,
            nome="Fabio",
            email="fabio@fabio.com"
        )
    ]


@router.post("/usuarios", response_model=UserResponse)
def create(user: UserRequest):
    return [
        UserResponse(
            id=2,
            nome=user.nome,
            email=user.email
        )
    ]
