import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS CATS (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
size INTEGER NOT NULL,
fluffiness INTEGER NOT NULL,
sociability INTEGER NOT NULL,
allergenicity INTEGER NOT NULL,
timelife INTEGER NOT NULL,
vaccinations TEXT NOT NULL
)
''')
cursor.execute("SELECT * FROM CATS")
cats = cursor.fetchall()
print(*cats)
connection.close()
