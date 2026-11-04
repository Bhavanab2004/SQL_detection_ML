
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_connection():
    return sqlite3.connect("users.db")

@app.route("/", methods=["GET", "POST"])
def login():

    message = ""
    query = ""
    success = False

    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")
        mode = request.form.get("mode", "secure")

        conn = get_connection()
        cursor = conn.cursor()

        try:
            if mode == "vulnerable":

                query = (
                    "SELECT * FROM users WHERE username = '"
                    + username
                    + "' AND password = '"
                    + password
                    + "'"
                )

                cursor.execute(query)

            else:

                query = """
                SELECT * FROM users
                WHERE username = ? AND password = ?
                """

                cursor.execute(query, (username, password))

            user = cursor.fetchone()

            if user:
                message = "Hi, " + str(user[1]) + "! Login Successful."
                success = True
            else:
                message = "Invalid username or password."

        except sqlite3.Error:
            message = "Database error occurred."

        finally:
            conn.close()

    return render_template(
        "index.html",
        message=message,
        query=query,
        success=success
    )


if __name__ == "__main__":
    app.run(debug=False)
