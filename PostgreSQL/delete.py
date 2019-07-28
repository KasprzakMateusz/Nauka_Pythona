from db import connection

cursor = connection.cursor()
cursor.execute("DELETE FROM budget WHERE id = 12")
connection.commit()
cursor.execute("SELECT * FROM budget")
results = cursor.fetchall()

for result in results:
    print(result)


