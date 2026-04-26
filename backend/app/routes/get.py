from fastapi import APIRouter, HTTPException, Form
from services import get_service

router = APIRouter(tags=["get"])


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/recordings/{prompt_id}")
# Gets all recordings for a specified prompt
def get_recordings_by_prompt(prompt_id: int ):
    try:
        return get_service.list_recordings_by_prompt(prompt_id)

    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
    
@router.get("/prompts/{prompt_id}/{person_name}")
def get_persons_recording(prompt_id: int, person_name: str):
    try:
        return get_service.list_recordings_by_prompt(prompt_id, person_name)

    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))

