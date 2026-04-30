from app.database import recordings

def list_recordings_by_prompt(prompt_id):
    db_res = recordings.select_prompts_recordings(prompt_id)

    recordings_dicts = [{"recording_id": str(recording_id), "person_name": person_name, "created_at": created_at.strftime("%H:%M %d %A %Y"), "storage_ref": storage_ref} for (recording_id, person_name, created_at, storage_ref) in db_res]
    
    return recordings_dicts      
