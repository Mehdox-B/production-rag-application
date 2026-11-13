from fastapi import FastAPI
from dotenv import load_dotenv
from helpers.config import get_settings
# load_dotenv(".env.dev")

settings = get_settings()

from src.routes.base import base_router
from src.routes.data import data_router


app = FastAPI()
app.include_router(base_router)
app.include_router(data_router)
