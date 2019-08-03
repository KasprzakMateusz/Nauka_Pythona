from db import conn
import datetime
import time

cursor = conn.cursor()
class Login:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.my_id = None

    def log(self):
        cursor.execute("SELECT id, login, password FROM user_game")
        result = cursor.fetchall()
        for x in result:
            if x[1] == self.name and x[2] == self.password:
                self.my_id = x[0]
                return self.my_id
                break
            else:
                None


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS user_game "
                   "(id SERIAL PRIMARY KEY, "
                   "login TEXT, "
                   "password TEXT, "
                   "metal TEXT, "
                   "stone TEXT, "
                   "hel3 TEXT, "
                   "rubbish TEXT, "
                   "gold TEXT, "
                   "silicon TEXT, "
                   "premium TEXT,"
                   "experience TEXT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS builds "
                   "(id TEXT, "
                   "name_1 TEXT, "
                   "name_2 TEXT)")
    conn.commit()



def fill_table(name, passwd):
    metal = "1"
    stone = "5"
    hel3 = "8"
    rubbish = "22"
    gold = "0"
    silicon = "0"
    premium = str(datetime.date(2019,8,12))

    cursor.execute("INSERT INTO user_game (login, password, metal, stone, hel3, rubbish, gold, silicon, premium, experience) VALUES "
                   "('"+name+"','"+passwd+"','"+metal+"','"+stone+"','"+hel3+"','"+rubbish+"','"+gold+"','"+silicon+"','"+premium+"','0')")
    conn.commit()


def read_statistics(x):
    now_date = datetime.date.today()
    cursor.execute("SELECT * FROM user_game")
    all_information = cursor.fetchall()
    for information in all_information:
        if x == information[0]:
            print(f'Nick: {information[1]}, ID: {information[0]} \n'
                  f'Twoje surowce: \nMetal: {information[3]} \nKamień: {information[4]} \nHel3: {information[5]} \nZłom: {information[6]} \nZłoto: {information[7]} \nKrzem: {information[8]}\n\n '
                  f'Twoje premium jest aktywne do: {information[9]}')

            datetime_object = datetime.datetime.strptime(information[9], "%Y-%m-%d").date()
            print(f'Aktywne do: {datetime_object}')
            print(f'Dziś jest: {now_date}')
            now_date = datetime_object - now_date
            print(f'Pozostało {now_date} dni premium')
            break


def materials_mining():
    cursor.execute("SELECT metal, id FROM user_game")
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


class Builds:
    def __init__(self,id):
        self.id = id
        self.name_1 = 0
        self.name_2 = 0

    def build(self):
        cursor.execute("SELECT * FROM builds")
        result = cursor.fetchall()

        if not result:
            cursor.execute("INSERT INTO builds (id, name_1, name_2) VALUES ('" + str(self.id) + "','0','0')")
            conn.commit()

        else:
            for x in result:
                if int(x[0]) == self.id:
                    self.name_1 = x[1]
                    self.name_2 = x[2]
                break
            else:
                print("erroro")
                cursor.execute("INSERT INTO builds (id, name_1, name_2) VALUES ('" + str(self.id) + "','0','0')")
                conn.commit()