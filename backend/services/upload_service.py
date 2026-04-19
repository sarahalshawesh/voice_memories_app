from pathlib import Path
import random
import string


def save_recording(file):
    # validate upload rules, check extension and content type
    content_type_options = ["audio/webm", "audio/wav", "audio/mpeg"]
    suffix_options = [".mp3", ".wav", ".webm"]
    file_suffix = Path(file.filename).suffix
    if file.content_type in content_type_options and file_suffix in suffix_options:
        
    # create unique storage name
        digits = string.digits
        random_num = ''.join(random.choice(digits) for i in range(10))
        stem_filename = Path(file.filename).stem.strip()
        storage_name = f"{stem_filename}-{random_num}{file_suffix}"

    # return structured result
        return {"file_storage_name": storage_name}
    
    else:
        raise ValueError("Unable to use audio: incorrect file type")
