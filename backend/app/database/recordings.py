import psycopg2
from config import DB_CONNECTION_STRING

def connect():
    return psycopg2.connect(DB_CONNECTION_STRING)


def insert_recordings(person_name_validated, prompt_id, file_content_type, file_size, storage_ref):
    sql = "INSERT INTO recordings(prompt_id, person_name, content_type, size_bytes, storage_ref) VALUES(%s, %s, %s, %s, %s) RETURNING recording_id, created_at;", ({prompt_id}, {person_name_validated}, {file_content_type}, {file_size}, {storage_ref}) 

    
    
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchone()
        
        
    
        conn.commit()
        return res
    
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        return error

    finally:
        cur.close()
        conn.close()