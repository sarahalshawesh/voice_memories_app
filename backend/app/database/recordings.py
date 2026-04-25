import psycopg2
from config import DB_CONNECTION_STRING

def connect():
    return psycopg2.connect(DB_CONNECTION_STRING)


def insert_recordings(person_name_validated, prompt_id, file_content_type, file_size, storage_ref):
    sql = f"INSERT INTO recordings(prompt_id, person_name, content_type, size_bytes, storage_ref), VALUES({prompt_id}, {person_name_validated}, {file_content_type}, {file_size}, {storage_ref})"
    
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)