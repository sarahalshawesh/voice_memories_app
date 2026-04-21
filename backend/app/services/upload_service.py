from pathlib import Path
import random
import string
from config import UPLOAD_DIR


async def save_recording(file, person_name):
    file_suffix = Path(file.filename).suffix.lower()
    person_name_validated = validate_person_name(person_name)
    validate_audio_file(file, file_suffix)
    file_storage_name = create_storage_name(file, file_suffix)
    await store_file(file, file_storage_name)
    # return structured result
    return {"file_storage_name": file_storage_name, "person_name": person_name_validated}

# Helper function that removes whitespace and ensures thee is input
def validate_person_name(person_name):
    stripped_person_name = person_name.strip()
    if stripped_person_name:
        return stripped_person_name
    

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
    