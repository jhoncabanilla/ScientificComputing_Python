import socket

# Creamos el objeto tipo socket
# > AF_INET: el socket va a ir a traves de Internet
# > SOCK_STREAM: serie de caracteres que se enviaran uno tras otro
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecemos la conexion a traves del puerto 80
mySock.connect( ('bing.com', 80) )