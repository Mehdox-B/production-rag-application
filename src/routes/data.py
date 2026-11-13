from fastapi import FastAPI,APIRouter,Depends,UploadFile
from helpers.config import get_settings,Settings

data_router = APIRouter(
    prefix="api/v1/data",
    tags=["api","v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_file(project_id:str 
                      , file:UploadFile
                      , settings:Settings = Depends(get_settings)):
    # Validate and check File Requirements
    pass