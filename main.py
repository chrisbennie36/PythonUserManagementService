from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from Data.Repositories.UserRepository import UserRepository
from Domain.Dtos.UserDto import UserDto
import logging
from werkzeug.exceptions import NotFound

app = FastAPI()
user_repository = UserRepository()

logger = logging.getLogger(__name__)

def initialiseLogger():
    logging.basicConfig(filename='user-management-service-log.log', level=logging.INFO)
    logger.info('Logger initialised')

initialiseLogger()

@app.get("/user/{user_id}")
def GetUser(user_id: int):
    try:
        return user_repository.getUserById(user_id)
    except NotFound:
        return JSONResponse(status_code = status.HTTP_404_NOT_FOUND, content = None)

@app.post("/user/", status_code = status.HTTP_201_CREATED)
def AddUser(user_dto: UserDto):
    user_repository.addUser(user_dto)

@app.put("/user/{user_id}", status_code = status.HTTP_200_OK)
def UpdateUserUsername(user_id: int, user_dto: UserDto):
    user_repository.updateUserUsername(user_id, user_dto)

@app.delete("/user/{user_id}", status_code = status.HTTP_200_OK)
def DeleteUser(user_id: int):
    try:
        user_repository.deleteUser(user_id)
    except NotFound:
        return JSONResponse(status_code = status.HTTP_404_NOT_FOUND, content = None)