import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
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
print("Database created successfully")
username = input("Enter username: ")
password = input("Enter password: ")
query = (
    "SELECT * FROM users WHERE username = '"
    + username
    + "' AND password = '"
    + password
    + "'"
)

print("\nGenerated SQL Query:")
print(query)

cursor.execute(query)

user = cursor.fetchone()

if user:
    print("\nLogin Successful!")
    print("Welcome:", user[1])
else:
    print("\nInvalid username or password")

conn.close()
