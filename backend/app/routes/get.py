from fastapi import APIRouter, HTTPException, Form
from backend.app.services import get_service

router = APIRouter(prefix="/get", tags=["get"])


@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/prompts/")
def get_all_recordings():
    try:
        get_service.list_recordings()
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))

@router.get("/prompts/{prompt_id}/recordings")
# Gets all recordings for a specified prompt
def get_recordings_by_prompt(prompt_id: int = Form(...)):
    try:
        get_service.list_recordings_by_prompt(prompt_id)

    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
    
@router.get("/prompts/{prompt_id}/{person_name}")
def get_persons_recording():
    try:
        get_service.list_recordings_by_prompt(prompt_id, person_name)

    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))

