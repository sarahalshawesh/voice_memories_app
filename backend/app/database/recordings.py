import psycopg2
from config import DB_CONNECTION_STRING

def connect():
    return psycopg2.connect(DB_CONNECTION_STRING)


def insert_recording(person_name_validated, prompt_id, file_content_type, file_size, storage_ref):
    conn, cur = None, None
    sql = "INSERT INTO recordings(prompt_id, person_name, content_type, size_bytes, storage_ref) VALUES(%s, %s, %s, %s, %s) RETURNING recording_id, created_at;"
    
    values = (prompt_id, person_name_validated, file_content_type, file_size, storage_ref) 

    
    
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, values)
        res = cur.fetchone()
        
        
    
        conn.commit()
        if res:
            return {"recording_id": res[0], "created_at": res[1]}
    
    except (Exception, psycopg2.DatabaseError) as error:
        if conn:
            conn.rollback()
        raise error

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        