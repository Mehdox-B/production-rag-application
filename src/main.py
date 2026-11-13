from fastapi import FastAPI
from dotenv import load_dotenv
from helpers.config import get_settings
# load_dotenv(".env.dev")

settings = get_settings()

from src.routes.base import base_router


app = FastAPI()
app.include_router(base_router)
