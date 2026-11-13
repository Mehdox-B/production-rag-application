from fastapi import FastAPI,APIRouter,Depends
import os
from helpers.config import Settings
from helpers.config import Settings, get_settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api","v1","base"]
)

@base_router.get("/")
#-------Settings Class Depedency Injection----------#
async def welcome(settings: Settings = Depends(get_settings)): 
    return {
        "application_name": settings.APPLICATION_NAME,
        "application_version": settings.APPLICATION_VERSION,
        "maintainer": settings.MAINTAINER,
    }