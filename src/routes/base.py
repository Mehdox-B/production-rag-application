from fastapi import FastAPI,APIRouter
import os

base_router = APIRouter(
    prefix="/api/v1",
    tags=["base_api_v1"]
)

@base_router.get("/")
async def welcome():
    application_name = os.getenv("APPLICATION_NAME")
    application_version = os.getenv("APPLICATION_VERSION") 
    return {
        "application_name": application_name,
        "application_version": application_version,
        "maintainer": os.getenv("USERNAME"),
    }