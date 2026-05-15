import sqlite3

conn = sqlite3.connect('food_to_ngo.db')
cursor = conn.cursor()

# Drop existing tables if they exist (to start fresh)
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS food_items")
cursor.execute("DROP TABLE IF EXISTS restaurants")
cursor.execute("DROP TABLE IF EXISTS ngos")
cursor.execute("DROP TABLE IF EXISTS users")

# Create users table
cursor.execute('''
    CREATE TABLE users (
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

# Create restaurants table
cursor.execute('''
    CREATE TABLE restaurants (
        restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        restaurant_name TEXT NOT NULL,
        certificate TEXT,
        is_verified INTEGER DEFAULT 1,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# Create ngos table
cursor.execute('''
    CREATE TABLE ngos (
        ngo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        ngo_name TEXT NOT NULL,
        total_capacity_smu REAL DEFAULT 0,
        remaining_capacity_smu REAL DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# Create food_items table
cursor.execute('''
    CREATE TABLE food_items (
        food_id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant_id INTEGER NOT NULL,
        food_name TEXT NOT NULL,
        food_type TEXT,
        shelf_life_hours INTEGER,
        dry_or_wet TEXT,
        calorific_value REAL,
        smu_equivalent REAL,
        quantity_available_smu REAL,
        expiry_time TIMESTAMP,
        FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
    )
''')

# Create orders table
cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ngo_id INTEGER NOT NULL,
        food_id INTEGER NOT NULL,
        quantity_smu REAL,
        otp TEXT,
        otp_expiry TIMESTAMP,
        order_status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (ngo_id) REFERENCES ngos(ngo_id),
        FOREIGN KEY (food_id) REFERENCES food_items(food_id)
    )
''')

conn.commit()
print("All tables created successfully!")

# Show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("\nTables created:")
for table in tables:
    print(f"  - {table[0]}")

conn.close()
