import sqlite3

def authenticate(
        username,
        password
):
    conn = sqlite3.connect(
        "database/users.db"
    )
    cursor = conn.cursor()
    cursor.execute("""
        SELECT password, role
        FROM users
        WHERE username = ?
    """,
    (username,)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        db_password = user[0]
        role = user[1]
        if password == db_password:
            return role
        return None 