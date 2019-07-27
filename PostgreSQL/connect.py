import psycopg2

connection = psycopg2.connect(user = "mateusz",
                                  password = "user",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "nauka")
on = False
if on:
    cursor = connection.cursor()
    model = input("Model: ")
    price = input("Price: ")
    create_table = "CREATE TABLE IF NOT EXISTS smartphones (id SERIAL PRIMARY KEY, model TEXT, price TEXT)"
    values = "INSERT INTO smartphones (model, price) VALUES ('"+model+"','"+price+"')"

    cursor.execute(create_table)
    cursor.execute(values)
    connection.commit()

cursor = connection.cursor()
cursor.execute("SELECT * FROM smartphones")
records = cursor.fetchall()

for record in records:
    print("ID: {} \nModel: {}\nPrice: {}".format(record[0],record[1],record[2]))
