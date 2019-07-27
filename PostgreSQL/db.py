import psycopg2

connection = psycopg2.connect(user = "mateusz",
                                  password = "user",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "nauka")
