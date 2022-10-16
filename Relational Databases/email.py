import sqlite3

# Establecemos una conexion con la base de datos
# --> 1. Esta base de datos la creamos previamente mediante el DB Browser
# --> 2. Si no esta creada, nos crea un nuevo archivo con el nombre indicado
conect = sqlite3.connect('emaildb.sqlite')
cur = conect.cursor() # Esta variable sera como un manejador a la hora de realizar consultas a la BD.

# Como primera consulta tenemos la siguiente, en la cual indicamos que si existe ya una tabla 'Counts' que la borre y pasamos a crear una nueva
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# Procedemos a leer el fichero
fname = input('Nombre del fichero: ')
if len(fname) < 1:
    print('Introduzca un fichero valido')
    exit(1)

fich = open(fname)
for line in fich:
    # Obtenemos solamente las lineas que comienzan por 'From: '
    if not line.startswith('From: '): continue

    # En caso de tener un linea con el formato que nos interesa tendremos algo como lo siguiente: 'From: stephen.marquard@uct.ac.za'
    # Por ello, realizamos un split y obtenemos la parte del email
    pieces = line.split()
    email = pieces[1]

    # Una vez obtenido el email, comprobamos si ya esta en la base de datos, en cuyo caso aumentaremos su contador, y sino esta, lo añadimos
    # con un contador de 1
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) # SQL Injection
    row = cur.fetchone() # Mediante este metodo, obtenemos las filas de la consulta realizada o si no hay mas filas obtenemos None

    if row is None:
        # El correo no esta en la base de datos
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))

    else:
        # Actualizamos el contador
        cur.execute('UPDATE Counts SET count = count+1 WHERE email = ? ', (email,))

    conect.commit()

# Finamente, mostramos las 10 primeras filas de la tabla Counts
cur.execute('SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10')
# De esta manera hacemos lo mismo que con el metodo fetchone()
for row in cur:
    print(str(row[0]), row[1])

# Fin conexion
cur.close()