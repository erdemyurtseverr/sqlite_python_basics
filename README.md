# SQLite User Management Example (Python)

This project is a simple example that shows how to use SQLite with Python.
It is created for learning purposes and focuses on basic database operations.

## Features
- Create a table using SQLite
- Insert multiple records with `executemany()`
- Prevent duplicate emails using a `UNIQUE` constraint
- Handle database errors with `try / except`
- Select and filter data using SQL `WHERE`
- Fetch results using `fetchone()`

## Technologies
- Python 3
- SQLite (sqlite3 module)

## How It Works
- The program connects to an SQLite database
- A `users` table is created if it does not exist
- Sample user data is inserted into the table
- Duplicate email entries are prevented
- Users between the ages of 18 and 20 are selected
- The result is printed to the console

## Example SQL Query
```sql
SELECT name FROM users WHERE age > 18 AND age < 20;

Example output:
('Özge',)

Language Note:
The code comments and documentation are written in simple English.
My current English level is around B1–B1+, and I am actively improving it.

Notes:
The database file (.db) is ignored using .gitignore
This project is intended for practice and learning

