from db import conn
import datetime
import time

class test:
    storage = 1
    def login():
        log_in = input("Login: ")
        password = input("Hasło: ")
        cursor = conn.cursor()
        cursor.execute("SELECT id, login, haslo FROM game")
        result = cursor.fetchall()
        for x in result:
            if x[1] == log_in and x[2] == password:
                storage = x[0]
                print(storage)
                break
            else:
                None

class Login:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def log(self):
        cursor = conn.cursor()
        cursor.execute("SELECT id, login, haslo FROM game")
        result = cursor.fetchall()
        for x in result:
            if x[1] == self.name and x[2] == self.password:
                storage = x[0]
                return(storage)
                break
            else:
                None


def create_table():
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS game (id SERIAL PRIMARY KEY, login TEXT, haslo TEXT, metal TEXT, kamien TEXT, hel3 TEXT, zlom TEXT, zloto TEXT, krzem TEXT, premium TEXT)")
    conn.commit()
    cursor.close()


def fill_table():
    cursor = conn.cursor()
    name = "M216"
    passwd = "123"
    metal = "1"
    stone = "5"
    hel3 = "8"
    rubbish = "22"
    gold = "0"
    silicon = "0"
    premium = str(datetime.date(2019,8,12))

    cursor.execute("INSERT INTO game (login, haslo, metal, kamien, hel3, zlom, zloto, krzem, premium) VALUES "
                   "('"+name+"','"+passwd+"','"+metal+"','"+stone+"','"+hel3+"','"+rubbish+"','"+gold+"','"+silicon+"','"+premium+"')")
    conn.commit()


def read_statistics(x):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game")
    all_information = cursor.fetchall()
    for information in all_information:
        if x == information[0]:
            print("Nick: {}, ID: {} \n"
                  "Twoje surowce: \nMetal: {:.4} \nKamień: {} \nHel3: {} \nZłom: {} \nZłoto: {} \nKrzem: {} \n\n"
                  "Twoje premium jest aktywne do: {}\n".format(information[1],information[0],information[3],information[4],information[5],information[6],information[7],information[8],information[9]))
            break


def materials_mining():
    cursor = conn.cursor()
    cursor.execute("SELECT metal, id FROM game")
    metal_db = cursor.fetchall()
    for x in metal_db:
        metal_value = 0.2
        metal = float(x[0]) + metal_value
        cursor.execute("UPDATE game SET metal = "+str(metal)+" WHERE id = "+str(x[1])+"")
        conn.commit()


def timer():
    while True:
        time.sleep(3)
        materials_mining()


