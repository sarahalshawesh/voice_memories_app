from database import recordings


def delete_recording_by_id(recording_id):
    recordings.delete_recording_in_db(recording_id)
    