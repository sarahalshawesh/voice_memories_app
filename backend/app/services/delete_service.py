from database import recordings


def delete_recording_by_id(recording_id):
    storage_ref = recordings.delete_recording_in_db(recording_id)
    if storage_ref == None:
        return False
    
    