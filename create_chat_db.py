import sqlite3
conn = sqlite3.connect(
    "database/chat_history.db"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
id INTEGER PRIMARY KEY,
username TEXT,
question TEXT,
answer TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()