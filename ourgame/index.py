from connect import conn


_cursor = conn.cursor()

class FillDatebase:

    def create_table(self):
        # Tworzy tabelę "game" w bazie danych "gra" która jest wyciągnięta z pliku connect.py
        _cursor.execute("CREATE TABLE IF NOT EXISTS game (id SERIAL PRIMARY KEY, name TEXT, password TEXT, register_date TEXT)")
        conn.commit()


class RegisterToGame:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.date = "04-08-2019"


    def create_user(self):
        # Wybierz wszystkie parametry umieszone w  kolumnie "name" z tabeli game.
        _cursor.execute("SELECT name FROM game")
        result = _cursor.fetchall()
        for x in result:
            if self.name == x[0]:
                print("Login istnieje, wybierze inny")
                break
        else:
            # Dodaje do tabeli 'game', wiersz który odnosi się do kolumn "name, password, register_date" - czyli Tworzenie nowego gracza
            _cursor.execute("INSERT INTO game (name, password, register_date) VALUES ('"+self.name+"','"+self.password+"','"+self.date+"')")
            conn.commit() # Importowanie wyżej podanych danych do bazy danych
            print(f'Użytkownik {self.name} stworzony')

class LoginToGame:

    def __init__(self,login,password):
        self.login = login
        self.password = password
        self.id = None

    def check_login(self):

        _cursor.execute("SELECT id, name, password FROM game")
        result = _cursor.fetchall()

        for x in result:
            if self.login == x[1] and self.password == x[2]:
                self.id = x[0]
        else:
            print("Złe dane")