import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


cursor.execute('INSERT INTO CATS (name, size, fluffiness, sociability, allergenicity, timelife) VALUES (?, ?, ?, ?, ?, ?)',
               ('1', 2, 3, 4, 5, 6))
#сюда короче про породы инфу заливать да
#fluffines 0-1-2
#sociability 1-2-3-4-5
#allergenicity 0-1-2-3-4
#timelife - время жизни
# cursor.execute("DELETE FROM CATS")
connection.commit()

cursor.execute("SELECT * FROM CATS")
cats = cursor.fetchall()
print(cats)
connection.close()