from fastapi import FastAPI,APIRouter,Depends
import os
from helpers.config import get_settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["base_api_v1"]
)

@base_router.get("/")
async def welcome(settings = Depends(get_settings)): 
    return {
        "application_name": settings.APPLICATION_NAME,
        "application_version": settings.APPLICATION_VERSION,
        "maintainer": settings.MAINTAINER,
    }