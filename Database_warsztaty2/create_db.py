from psycopg2 import connect, errors

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
sql_code1 = """CREATE DATABASE new_database;"""
sql_code2 = """CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    hashed_password VARCHAR(80)
    );
"""
sql_code3 = """CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    from_id INT,
    to_id INT,
    creation_date TIMESTAMP,
    text VARCHAR(255),
    FOREIGN KEY (from_id) REFERENCES users(id),
    FOREIGN KEY (to_id) REFERENCES users(id)
    );
"""

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST)
    cursor = cnx.cursor()
    cnx.autocommit = True
    cursor.execute(sql_code1)
    print("Database create!")
except errors.DuplicateDatabase:
    print("Database already exists!")
except errors.OperationalError:
    print("Connection Error")
else:
    cursor.close()
    cnx.close()


try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST, database='new_database')
    cursor = cnx.cursor()
    cnx.autocommit = True
    try:
        cursor.execute(sql_code2)
        print("Table users created!")
    except errors.DuplicateTable:
        print("Table already exists!")

    try:
        cursor.execute(sql_code3)
        print("Table messages created!")
    except errors.DuplicateTable:
        print("Table already exists!")

except errors.OperationalError:
    print("Connection Error")
else:
    cursor.close()
    cnx.close()
