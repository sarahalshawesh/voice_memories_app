from pathlib import Path
import random
import string


def save_recording(file):
    # validate upload rules, check extension and content type
    content_type_options = ["audio/webm", "audio/wav", "audio/mpeg"]
    suffix_options = [".mp3", ".wav", ".webm"]
    try:
        if file.content_type in content_type_options and (Path(file.filename).suffix in suffix_options):
        
    # create unique storage name
            digits = string.digits
            random_num = random.choice(digits, k=10)
            storage_name = f"{random_num}{file.filename}"

    # return structured result
            return {"filename": storage_name}
    except Exception as error:
        print("An exception occurred:", type(error).__name__, ":", error)