import sqlite3
#We'll code technical steps about sqlite.
con=sqlite3.connect("user_data.db")
cursor=con.cursor()
#We'll create a table for our database.

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    loc TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
    )
"""
               )

#In here we finally add some person datas to our table that we created before.
#With .executemany we add datas more than one while we use it we also used
#INSERT INTO which is a command in SQL & SQLite

users=[
    ("Erdem",18,"12.cd","0577 777 7777","eridem.@umail.com"),
    ("Murat",22,"13.cd","0666 666 6666","mjurat.@umail.com"),
    ("Özge",19,"14.cd","0555 555 5555","ozzke@umail.com")
       ]
try:

    cursor.executemany("""
    INSERT INTO users (name, age, loc, phone, email)
    VALUES (?,?,?,?,?)
    """,users
    )
    con.commit()
except sqlite3.IntegrityError as w:
    print("Insert failed because of :",w)


#Let's continue with Select and where
#I want to select and filter datas so I used ıt these
#At the end while we run this program it will show us Özge (19 years old)

cursor.execute("SELECT name FROM users WHERE age>18 and age<20")
print(cursor.fetchone())
cursor.close()
con.close()