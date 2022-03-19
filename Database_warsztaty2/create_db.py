from psycopg2 import connect, errors

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
sql_code1 = """CREATE DATABASE New_Database;"""

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST)
    cursor = cnx.cursor()
    cnx.autocommit = True
    cursor.execute(sql_code1)
    print("Database create!")
except errors.DuplicateDatabase:
    print("Database already exists!")
else:
    cursor.close()
    cnx.close()


