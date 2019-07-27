import psycopg2

connection = psycopg2.connect(user = "mateusz",
                                  password = "user",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "nauka")

on = True
add = True
if on:
    cursor = connection.cursor()
    create_table = "CREATE TABLE IF NOT EXISTS smartphones (id SERIAL PRIMARY KEY, model TEXT, price TEXT)"
    cursor.execute(create_table)
    model = input("Model: ")
    cursor.execute("SELECT model FROM smartphones")
    records = cursor.fetchall()
    b = 0
    for record in records:
        if model == record[b]:
            print("Taki model już istnieje")
            add = False
            cursor.close()
            break

    if add:
        price = input("Price: ")
        values = "INSERT INTO smartphones (model, price) VALUES ('"+model+"','"+price+"')"
        cursor.execute(values)
        connection.commit()

cursor = connection.cursor()
cursor.execute("SELECT * FROM smartphones")
records = cursor.fetchall()

for record in records:
    print("ID: {} \nModel: {}\nPrice: {}".format(record[0],record[1],record[2]))
