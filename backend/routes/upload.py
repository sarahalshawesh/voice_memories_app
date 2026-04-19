from fastapi import APIRouter, UploadFile, File
from services.upload_service import upload_service


# Creates the router with a prefix so all routes begin with upload
router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/")
# Creates the function for uploading a recording. Requires a file input.
async def upload_recording(file: UploadFile = File(...)):
    res = await upload_service.save_recording(file)
    return res
    
