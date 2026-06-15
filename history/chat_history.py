import sqlite3

def save_chat(
        username,
        question,
        answer
):
    conn = sqlite3.connect(
        "database/chat_history.db"
    )
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chat_history
    (
        username,
        question,
        answer
    )
    VALUES (
        ?,
        ?,
        ?)
    """, 
    (
        username, 
        question, 
        answer
    ))
    conn.commit()
    conn.close()