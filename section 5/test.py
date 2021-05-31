import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE users(id integer primary key, username text, password text)'
cursor.execute(create_table)

user = ('jose', 'asdf')
insert_query = "INSERT INTO users VALUES(NULL, ?, ?)"
cursor.execute(insert_query, user)

users = [
    ('fredson', '1234'),
    ('anne', '1234')
]

cursor.executemany(insert_query, users)

connection.commit()
connection.close()