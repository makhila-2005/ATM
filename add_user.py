import sqlite3

conn = sqlite3.connect("atm.db")
cur = conn.cursor()

name = input("Enter name: ")
pin = input("Enter PIN: ")
balance = int(input("Enter balance: "))

cur.execute(
    "INSERT INTO users (name, pin, balance) VALUES (?, ?, ?)",
    (name, pin, balance)
)

conn.commit()
conn.close()

print("User added successfully!")
