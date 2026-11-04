### 1. Introduction

This Python file is used to demonstrate a SQL Injection attack using a simple login application.

Python provides a built-in library called `sqlite3`, which allows us to create and interact with SQLite databases. We do not need to install a separate database server.

### 2. Import the library

```python
import sqlite3
```

We import the `sqlite3` library to connect Python with the SQLite database.

### 3. Establish the database connection

```python
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
```

- `sqlite3.connect("users.db")` establishes a connection with the database. If it does not exist, it creates one.
- `conn.cursor()` creates a cursor object that allows Python to execute SQL queries.

### 4. Create the database structure

We create a table named `users` containing three columns:

- ID
- Username
- Password

### 5. Insert user records

We insert two sample users into the database:

| Username | Password |
|---|---|
| admin | admin123 |
| bhavana | pass123 |

We use `conn.commit()` to save the inserted records.

### 6. Execute the login query

The application accepts a username and password from the user and constructs an SQL query to verify the credentials.

### 7. Demonstrate SQL Injection

Instead of entering a valid username, we enter this payload in the username field:

```sql
' OR '1'='1' --
```

We enter any password.

The payload manipulates the SQL query:

- `'` closes the existing string.
- `OR` introduces an alternative condition.
- `'1'='1'` is an always-true condition.
- `--` comments out the remaining SQL statement.

As a result, the WHERE condition becomes TRUE, potentially allowing the attacker to bypass login authentication.

### 8. Retrieve the result

```python
user = cursor.fetchone()
```

This retrieves the first matching database record.

If a record is returned, the application displays Login Successful. Otherwise, it displays Invalid username or password.

### 9. Close the connection

```python
conn.close()
```

This closes the connection between Python and the SQLite database.
