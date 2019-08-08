import sqlite3

def connect(db_file):
    connection = sqlite3.connect(db_file)
    return connection

def create_base(connection, sql):
    conn = connection.cursor()
    conn.execute(sql)

class Quires:
    def __init__(self):
        pass

    def first_table(self):
        self.project1 = """CREATE TABLE IF NOT EXISTS p_1 (name text, surname text)"""
        self.project2 = """CREATE TABLE IF NOT EXISTS p_2 (name text, surname text)"""



# main code
def main():
    db_file = "sql.db"
    connection = connect(db_file)
    q = Quires()
    q.first_table()

    create_base(connection, q.project1)
    create_base(connection, q.project2)


if __name__ == '__main__':
    main()