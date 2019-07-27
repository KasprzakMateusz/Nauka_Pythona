from db import connection

cursor = connection.cursor()
cursor.execute("DELETE FROM budget WHERE id = 4")
connection.commit()
cursor.execute("SELECT * FROM budget")
results = cursor.fetchall()

print(results)


