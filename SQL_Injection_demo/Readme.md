# SQL Injection Demonstration

## What This Project Does

This project demonstrates how SQL Injection attacks work and how they can be prevented using secure SQL queries.

It provides a login interface with two modes:

- **Vulnerable Login:** Uses SQL query string concatenation, allowing specially crafted inputs to manipulate the SQL query and potentially bypass authentication.
- **Secure Login:** Uses parameterized SQL queries to prevent SQL Injection.

Users can enter login credentials and compare the behavior of both modes.

When login is successful, the application displays a personalized greeting:

`Hi, admin! Login Successful.`

When login fails, it displays an invalid credentials message.

## How to Run

### 1. Install Flask

```bash
pip install flask
```

### 2. Create the Database

```bash
python create_db.py
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

### Sample Login Credentials

| Username | Password |
|---|---|
| admin | admin123 |
| bhavana | pass123 |
