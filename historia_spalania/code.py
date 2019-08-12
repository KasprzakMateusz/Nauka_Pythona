import sqlite3


def connect(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except:
        print("Błąd bazy danych")



class Queries:
    db_file = "sql.db"
    connection = connect(db_file)

    def __init__(self):
        pass

    def sql_query(self, connection, sql):
        conn = connection.cursor()
        conn.execute(sql)

    def create_table(self):
        self.create_table_fuel_usage = '''CREATE TABLE IF NOT EXISTS fuel_usage (fuel_type text, fuel_amount text, 
                                        price_per_liter text, refueling_date text)'''

    def add_refueling(self, connection, fills):
        self.refueling = '''INSERT INTO fuel_usage (fuel_type, fuel_amount, 
                            price_per_liter, refueling_date) VALUES (?,?,?,?)'''
        conn = connection.cursor()
        conn.execute(self.refueling, fills)
        connection.commit()
        return conn.lastrowid

    def show_db(self, connection):
        ask = '''SELECT * FROM fuel_usage'''
        conn = connection.cursor()
        conn.execute(ask)
        result = conn.fetchall()
        for i in result:
            print(f'Rodzaj paliwa: {i[0]} \nIlość zatankowanego paliwa: {i[1]} \nCena za litr: {i[2]} \nData Tankowania: {i[3]}')
            print("-"*30)
            blach = f'Rodzaj paliwa: {i[0]} \nIlość zatankowanego paliwa: {i[1]} \nCena za litr: {i[2]} \nData Tankowania: {i[3]}'
            return blach

    def sum_of_refuel(self, connection):
        all_fuel = 0
        all_money = 0
        conn = connection.cursor()
        conn.execute("SELECT fuel_amount, price_per_liter FROM fuel_usage")
        result = conn.fetchall()
        for i in result:
            all_fuel = all_fuel + int(i[0])
            all_money = all_money + (int(i[0]) * int(i[1]))
        print(f'Ilość zatankowanego paliwa: {all_fuel}')
        print(f'Ilość zapłaconych PLNów: {all_money}')



# Main CODE

def main_create():
    db_file = "sql.db"
    connection = connect(db_file)
    q = Queries()
    q.create_table()
    q.sql_query(connection, q.create_table_fuel_usage)

def main_app():
    db_file = "sql.db"
    connection = connect(db_file)
    print("Witaj w kalkulatorze spalania!")
    print("Co chcesz zrobić? ")
    choose = input("1 - Dodaj tankowanie \n2 - sprawdź swoją historię \n3 - sprawdź ogólne statystyki")

    if choose == "1":
        fuel_type = input("1 - LPG \n2 - Benzyna \n3 - Diesel")

        if fuel_type == "1":
            fuel_type = "LPG"
        elif fuel_type == "2":
            fuel_type = "Benzyna"
        elif fuel_type == "3":
            fuel_type = "Diesel"

        fuel_amount = input("Podaj ilość zatankowanego paliwa: ")
        price_per_liter = input("Cena za 1 litr")
        refueling_date = input("Data w formacie rrrr-mm-dd")
        q = Queries()

        fills = (fuel_type, fuel_amount, price_per_liter, refueling_date)
        q.add_refueling(connection, fills)



        # print(f'typ paliwa: {fuel_type} ilość zatankowanego paliwa: {fuel_amount} cena za litr: {price_per_liter} data tankowania: {refueling_date}')
    elif choose == "2":
        print("-" * 30)
        q = Queries()
        q.sum_of_refuel(connection)
    elif choose == "3":
        print("-" * 30)
        q = Queries()
        q.show_db(connection)
    else:
        print("something went wrong!")




if __name__ == "__main__":
    main_app()