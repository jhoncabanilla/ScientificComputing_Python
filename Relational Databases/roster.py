import json
import sqlite3

# Conexion con la base de datos
conex = sqlite3.connect('rosterDB.sqlite')
cursor = conex.cursor()

# Procedemos a ejecutar el siguiente Script
cursor.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE
);

CREATE TABLE Member(
    user_id      INTEGER,
    course_id    INTEGER,
    role         INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Leemos el fichero
fname = input('Nombre del fichero: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# Obtenemos el json correspondiente
data = open(fname).read()
js = json.loads(data)

for item in js:
    name = item[0]
    title = item[1]
    role = item[2]

    # Insertamos en la base de datos
    # 1.User
    # Como name eos clave lgica y ademas es unique, en el caso de encontrar un valor para name repetido saltaria un error, pero si utilizamos
    # IGNORE evitamos ese error e ignoramos el valor repetido
    cursor.execute('INSERT OR IGNORE INTO User (name) VALUES (?) ', (name,))

    cursor.execute('SELECT ID FROM User WHERE name = ? ', (name,))
    user_id = cursor.fetchone()[0]
    print(user_id)
    # 2.Course
    cursor.execute('INSERT OR IGNORE INTO Course (title) VALUES (?) ', (title,))

    cursor.execute('SELECT ID FROM Course WHERE title = ? ', (title,))
    course_id = cursor.fetchone()[0]
    print(course_id)

    # 3.Member
    cursor.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

    conex.commit()