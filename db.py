import sqlite3 
import os 
 
DATABASE_PATH = 'food_to_ngo.db' 
 
def get_connection(): 
    try: 
        conn = sqlite3.connect(DATABASE_PATH) 
        conn.row_factory = sqlite3.Row 
        return conn 
    except sqlite3.Error as err: 
        print(f"Database Connection Error: {err}") 
        return None 
 
def get_cursor(): 
    conn = get_connection() 
    if conn: 
        return conn, conn.cursor() 
    return None, None 
 
def init_db(): 
    conn = get_connection() 
    cursor = conn.cursor() 
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS users ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            email TEXT UNIQUE NOT NULL, 
            password TEXT NOT NULL, 
            role TEXT NOT NULL, 
            certificate TEXT, 
            is_approved INTEGER DEFAULT 1, 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        ) 
    ''') 
    conn.commit() 
    conn.close() 
    print("Database initialized!") 
 
if not os.path.exists(DATABASE_PATH): 
    init_db() 
