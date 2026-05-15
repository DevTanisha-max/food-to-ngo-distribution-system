import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    try:
        print("DB NAME:", os.getenv("DB_NAME"))
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None


def get_cursor():
    conn = get_connection()
    if conn:
        return conn, conn.cursor(dictionary=True)
    return None, None


