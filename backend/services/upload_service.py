from pathlib import Path
from numpy import random 


def save_recording(file):
    # validate upload rules, check extension and content type
    content_type_options = ["audio/webm", "audio/wav", "audio/mpeg"]
    suffix_options = [".mp3", ".wav", ".webm"]
    if file.content_type in content_type_options and (Path(file).suffix in suffix_options):
        
    # create unique storage name
        random_num = random.randint(10, size=(5))
        storage_name = f"{file.filename}{random_num}"

    # return structured result
        return {"filename": storage_name}