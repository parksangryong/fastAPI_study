from fastapi import APIRouter
from pydantic import BaseModel
from common.exception.exceptions import BusinessException

router = APIRouter(prefix="/users")

class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("", status_code=201)
def create_user(user: CreateUserRequest):
    return user

class GetUserResponse(BaseModel):
    user_id: int

@router.get("/{user_id}")
def get_user(user_id: int) -> GetUserResponse:
    raise BusinessException("USER-001")