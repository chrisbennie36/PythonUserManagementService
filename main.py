from fastapi import FastAPI
from routers import users
import logging

app = FastAPI()
app.include_router(users.router)

logger = logging.getLogger(__name__)

def initialiseLogger():
    logging.basicConfig(filename='user-management-service-log.log', level=logging.INFO)
    logger.info('Logger initialised')

initialiseLogger()