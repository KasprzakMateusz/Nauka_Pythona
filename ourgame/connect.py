import psycopg2

conn = psycopg2.connect(user = "mateusz",
                        password = "user",
                        host = "localhost",
                        port = "5433",
                        database = "gra")


