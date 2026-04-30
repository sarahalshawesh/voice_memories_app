from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from app.services import upload_service


# Creates the router with a prefix so all routes begin with upload
router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/")
# Creates the function for uploading a recording. Requires a file input. 
async def upload_recording(file: UploadFile = File(...), person_name: str = Form(...), prompt_id: int = Form(...)):
    try: 
        res = await upload_service.save_recording(file, person_name, prompt_id)
        print(res)
        return res

    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))

    
