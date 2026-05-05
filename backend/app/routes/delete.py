from fastapi import APIRouter, HTTPException
from app.services import delete_service

router = APIRouter(prefix='/delete', tags=["delete"])

@router.delete("/{recording_id}")
# Deletes a specific recording using the recording id
def delete_recording(recording_id: str ):
    try:
        return delete_service.delete_recording_by_id(recording_id)

    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
    