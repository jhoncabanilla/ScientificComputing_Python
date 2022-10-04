import socket

# Creamos el socket con los parametros indicados y establecemos la conexion con el Servidor
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect( ('data.pr4e.org', 80) )

# HTTP Request
# > enconde(): prepara los datos para ir a traves de Internet
cmd ='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() 
mySocket.send(cmd)

# Recibimos la respuesta
while True:
    data = mySocket.recv(512) # Recibiremos 512 caracteres cada vez
    if (len(data) < 1):
        break
    print(data.decode()) # Decodificamos la informacion recibida para imprimirla

mySocket.close() # Cerramos finalmente el socket

