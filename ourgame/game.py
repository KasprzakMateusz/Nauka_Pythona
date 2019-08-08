from ourgame import index

name = input("Imie: ")
password = input("Hasło: ")

# fill = index.FillDatebase()
# fill.create_table()

fillregister = index.RegisterToGame(name,password)
fillregister.create_user()

# x = index.LoginToGame("Mateusz","123")
# x.check_login()


