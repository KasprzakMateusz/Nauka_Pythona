from db import connection

cursor = connection.cursor()
cursor.execute("SELECT * FROM smartphones")
results = cursor.fetchall()
for result in results:
    print(result)