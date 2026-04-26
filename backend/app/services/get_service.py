from database import select_prompts_recordings

def list_recordings_by_prompt(prompt_id):
    db_res = select_prompts_recordings(prompt_id)
    recordings = [{"recording_id": str(db_res.UUID), "person_name": db_res.person_name, "created_at": db_res.created_at} for r in db_res]
    return recordings        

    

def show_persons_recording(prompt_id, prompt_name):
    pass