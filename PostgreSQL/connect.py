from db import connection

on = True
add = True
if on:
    cursor = connection.cursor()
    create_table = "CREATE TABLE IF NOT EXISTS smartphones (id SERIAL PRIMARY KEY, model TEXT, price TEXT, operator TEXT)"
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


    if add:
        price = input("Price: ")
        operator = input("Operator: ")
        values = "INSERT INTO smartphones (model, price, operator) VALUES ('"+model+"','"+price+"','"+operator+"')"
        cursor.execute(values)
        connection.commit()

cursor = connection.cursor()
cursor.execute("SELECT * FROM smartphones")
records = cursor.fetchall()


for record in records:
    print("ID: {} \nModel: {}\nPrice: {}zł".format(record[0],record[1],record[2]))

