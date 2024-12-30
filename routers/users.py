from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from Data.Repositories.UserRepository import UserRepository
from Domain.Dtos.UserDto import UserDto
from werkzeug.exceptions import NotFound

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

user_repository = UserRepository()

@router.get("/{user_id}")
async def GetUser(user_id: int):
    try:
        return user_repository.getUserById(user_id)
    except NotFound:
        return JSONResponse(status_code = status.HTTP_404_NOT_FOUND, content = None)

@router.post("/", status_code = status.HTTP_201_CREATED)
def AddUser(user_dto: UserDto):
    user_repository.addUser(user_dto)

@router.put("/{user_id}", status_code = status.HTTP_200_OK)
def UpdateUserUsername(user_id: int, user_dto: UserDto):
    user_repository.updateUserUsername(user_id, user_dto)

@router.delete("/{user_id}", status_code = status.HTTP_200_OK)
def DeleteUser(user_id: int):
    try:
        user_repository.deleteUser(user_id)
    except NotFound:
        return JSONResponse(status_code = status.HTTP_404_NOT_FOUND, content = None)