import sqlite3

conn = sqlite3.connect("atm.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    pin TEXT,
    balance INTEGER
)
""")

cur.execute("INSERT INTO users (name, pin, balance) VALUES (?, ?, ?)",
            ("Akhila", "1234", 5000))

cur.execute("INSERT INTO users (name, pin, balance) VALUES (?, ?, ?)",
            ("Ravi", "4321", 8000))

conn.commit()
conn.close()

print("Database created successfully")
