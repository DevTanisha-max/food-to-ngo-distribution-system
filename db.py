import os
import sqlite3

# Check if running on Render (has DATABASE_URL)
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    # PostgreSQL for Render
    import psycopg2
    from psycopg2.extras import RealDictCursor
    
    def get_connection():
        return psycopg2.connect(DATABASE_URL)
    
    def get_cursor():
        conn = get_connection()
        return conn, conn.cursor(cursor_factory=RealDictCursor)
else:
    # SQLite for local development
    DATABASE_PATH = 'food_to_ngo.db'
    
    def get_connection():
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    
    def get_cursor():
        conn = get_connection()
        return conn, conn.cursor()