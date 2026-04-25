from fastapi import APIRouter, HTTPException, Form
from services import get_service

router = APIRouter(prefix="/get", tags=["get"])


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/prompts/{prompt_id}/recordings")
# Gets all recordings for a specified prompt
def get_recordings_by_prompt(prompt_id: int ):
    try:
        get_service.list_recordings_by_prompt(prompt_id)

    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
    
@router.get("/prompts/{prompt_id}/{person_name}")
def get_persons_recording(prompt_id: int, person_name: str):
    try:
        get_service.list_recordings_by_prompt(prompt_id, person_name)

    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))

