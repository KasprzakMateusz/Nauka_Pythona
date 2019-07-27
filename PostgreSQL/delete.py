from db import connection

cursor = connection.cursor()
cursor.execute("DELETE FROM smartphones WHERE id > 0")
connection.commit()
cursor.execute("SELECT * FROM smartphones")
results = cursor.fetchall()

print(results)


