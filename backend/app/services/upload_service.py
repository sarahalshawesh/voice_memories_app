from pathlib import Path
import random, string
from config import UPLOAD_DIR
from database import recordings


async def save_recording(file, person_name, prompt_id):
    file_suffix = Path(file.filename).suffix.lower()
    person_name_validated = validate_person_name(person_name)
    validate_audio_file(file, file_suffix)
    file_storage_name = create_storage_name(file, file_suffix)
    stored_file = await store_file(file, file_storage_name)
    storage_ref = stored_file.name
    file_content_type = file.content_type
    file_size = stored_file.stat().st_size
    try:
        insert_res = recordings.insert_recording(person_name_validated, prompt_id, file_content_type, file_size, storage_ref)
        print(insert_res)
        recording_id = insert_res.recording_id
        created_at = insert_res.created_at
        return {"recording_id": recording_id, "created_at": created_at}
    except Exception as e:
        return f"{e}: DB error inserting recording for {storage_ref}"
    

# Helper function that removes whitespace and ensures thee is input
def validate_person_name(person_name):
    stripped_person_name = person_name.strip()
    if stripped_person_name:
        return stripped_person_name
    raise ValueError("Person name cannot be empty")
    

 # Helper function to validate upload rules, check extension and content type
def validate_audio_file(file, file_suffix):
    content_type_options = ("audio/webm", "audio/wav", "audio/mpeg")
    suffix_options = [".mp3", ".wav", ".webm"]
    if not file.content_type.startswith(content_type_options) or file_suffix not in suffix_options:
        raise ValueError("Unable to use audio: incorrect file type")
    
# Helper function that creates a storage name
def create_storage_name(file, file_suffix):
    digits = string.digits
    random_num = ''.join(random.choice(digits) for i in range(10))
    stem_filename = Path(file.filename).stem.strip()
    file_storage_name = f"{stem_filename}-{random_num}{file_suffix}"
    return file_storage_name

async def store_file(file, file_storage_name):
    # reads the file and writes it to the chosen folder path
    UPLOAD_DIR.mkdir(exist_ok=True)
    filepath = UPLOAD_DIR / file_storage_name
    audio_content = await file.read()
    with open(filepath, "wb") as output_file:
        output_file.write(audio_content) 
    return filepath