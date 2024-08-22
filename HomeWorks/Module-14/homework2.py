import sqlite3
import random

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS Users")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", random.randint(20, 100), 1000))

cursor.execute("UPDATE Users SET balance = 500 WHERE (id % 2) = 1")

cursor.execute("DELETE FROM Users WHERE (id % 3) = 1")

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
temp1 = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
temp2 = cursor.fetchone()[0]
balance = temp2/temp1
cursor.execute("SELECT AVG(balance) FROM Users")

avg_balance = cursor.fetchone()[0]

print(avg_balance)

connection.commit()
connection.close()
