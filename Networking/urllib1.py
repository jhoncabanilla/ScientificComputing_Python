"""
>>>urllib<<<
Libreria que hace todo el trabajo del socket para nosotros y hace que las paginas web se vean como un fichero
"""
import urllib.request

"""
# Hace directamente el GET y lo codifica (encode()), es decir, realiza la conexion
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip()) # Recibimos bytes, por lo que tenemos que decodificar
# De esta manera obtenemos la informacion, pero no obtenemos la cabecera, anque sí que se puede conseguir.
"""

"EJERCICIO: Obtener un listado de cuales son las palabras mas comunes del texto"
dicc = dict()

# Conexicon mediante urllib
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

" 1: Creamos el diccionario y rellenamos con las palabras y sus recuentos correspondientes"
# Recorremos las lineas y vamos incluyendo las palabras en el diccionario mediante el metodo .get()
for line in fhand:
    words = line.decode().split()
    for word in words:
        dicc[word] = dicc.get(word, 0) + 1

" 2: Cuando lo tengamos, cramos el listado mediante funcion lambda"
print(sorted([(value, key) for (key, value) in dicc.items()], reverse=True))
