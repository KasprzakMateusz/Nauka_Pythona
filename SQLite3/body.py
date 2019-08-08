import sqlite3
from sqlite3 import Error

def main():
    database = "db.db"
    connection = create_connection(database)

    your_choose = input("1 - create table, 2 Insert to database, 3 show table tasks")

    if your_choose == "1":
        sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    begin_date text,
                                    end_date text
                                    );"""

        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        project_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""

        if connection is not None:
            create_table(connection, sql_create_projects_table)
            create_table(connection, sql_create_tasks_table)
        else:
            print("error!")
    elif your_choose == "2":

        with connection:
            project = ('Cool Apps with SQLite and Python','2019-08-08','2019-08-30');
            project_id = create_project(connection,project)

            task_1 = ('Analyze the requirments of the app',1,1,project_id,'2019-08-08','2019-08-10')
            task_2 = ('Confirm',1,1,project_id,'2019-08-10','2019-08-15')

            create_task(connection,task_1)
            create_task(connection,task_2)
    elif your_choose == "3":
        print_datebase(connection)
    else:
        print("Zły wybór")

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

def create_table(connection, create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_project(connection, project):
    sql = ''' INSERT INTO projects (name, begin_date, end_date) VALUES (?,?,?) '''
    cursor = connection.cursor()
    cursor.execute(sql, project)
    return cursor.lastrowid

def create_task(connection, task):
    sql = '''INSERT INTO tasks (name, priority, status_id, project_id, begin_date, end_date)
                            VALUES (?,?,?,?,?,?) '''
    cursor = connection.cursor()
    cursor.execute(sql, task)
    return cursor.lastrowid

def print_datebase(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    pri = cursor.fetchall()
    for x in pri:
        print(x)


if __name__ == "__main__":
    main()
