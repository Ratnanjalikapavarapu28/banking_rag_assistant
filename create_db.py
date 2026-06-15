import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO users 
(username, password, role)
VALUES
('admin', 'admin123', 'Admin')
""")

conn.commit()
conn.close()

print("✅ users.db created successfully")

               