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
                                        price_per_liter text, refueling_date text, mile_age text, full text)'''

    def add_refueling(self, connection, fills):
        self.refueling = '''INSERT INTO fuel_usage (fuel_type, fuel_amount, 
                            price_per_liter, refueling_date, mile_age, full) VALUES (?,?,?,?,?,?)'''
        conn = connection.cursor()
        conn.execute(self.refueling, fills)
        connection.commit()
        return conn.lastrowid

    def show_db(self, connection):
        ask = '''SELECT * FROM fuel_usage'''
        conn = connection.cursor()
        conn.execute(ask)
        result = conn.fetchall()
        list1 = []
        for i in result:
            history = f'Rodzaj paliwa: {i[0]} \nIlość zatankowanego paliwa: {i[1]} \nCena za litr: {i[2]} \nData Tankowania: {i[3]} \nPrzebieg: {i[4]} \nTankowanie do pełna: {i[5]} \n\n'
            list1.append(history)
        return list1

    def sum_of_refuel(self, connection):
        all_fuel = 0
        all_money = 0
        conn = connection.cursor()
        conn.execute("SELECT fuel_amount, price_per_liter FROM fuel_usage")
        result = conn.fetchall()
        for i in result:
            all_fuel = all_fuel + float(i[0])
            all_money = all_money + (float(i[0]) * float(i[1]))
        return f'Ilość zatankowanego paliwa: {all_fuel} Litrów \nIlość zapłaconych PLNów: {round(all_money, 2)} Zł'

    def checker(self, par):
        try:
            float(par)
            return True
        except ValueError:
            return False




# Main CODE

def main_create():
    db_file = "sql.db"
    connection = connect(db_file)
    q = Queries()
    q.create_table()
    q.sql_query(connection, q.create_table_fuel_usage)


if __name__ == "__main__":
    pass
