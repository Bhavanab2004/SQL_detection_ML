
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("DELETE FROM users")

cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ("admin", "admin123")
)

cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ("bhavana", "pass123")
)

conn.commit()

print("Database created successfully!")
print(cursor.execute("SELECT * FROM users").fetchall())

conn.close()
