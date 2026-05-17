import sqlite3
import os

DATABASE_PATH = 'food_to_ngo.db'

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_cursor():
    conn = get_connection()
    return conn, conn.cursor()

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
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurants (
            restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            restaurant_name TEXT NOT NULL,
            certificate TEXT,
            is_verified INTEGER DEFAULT 1
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ngos (
            ngo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            ngo_name TEXT NOT NULL,
            total_capacity_smu REAL DEFAULT 0,
            remaining_capacity_smu REAL DEFAULT 0
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_items (
            food_id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER NOT NULL,
            food_name TEXT NOT NULL,
            food_type TEXT,
            shelf_life_hours INTEGER,
            dry_or_wet TEXT,
            calorific_value REAL,
            smu_equivalent REAL,
            quantity_available_smu REAL,
            expiry_time TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ngo_id INTEGER NOT NULL,
            food_id INTEGER NOT NULL,
            quantity_smu REAL,
            otp TEXT,
            otp_expiry TIMESTAMP,
            order_status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized!")

# Initialize database if it doesn't exist
if not os.path.exists(DATABASE_PATH):
    init_db()
else:
    print("Database already exists")