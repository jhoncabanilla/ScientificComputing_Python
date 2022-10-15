import json
import urllib.request, urllib.parse

# URL de la API que vayamos a utilizar
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Introduzca ubicacion: ')
    if len(address) < 1: break # Comprobamos que la ubicacion introducida sea correcta

    # Concatenamos la url con el String resultante introducido para obtener el json correcto. Esto lo codificamos para respetar el formato de la url
    url = serviceurl + urllib.parse.urlencode({'address': address})

    # Establecemos la conexion mediante urlib, que nos devuelve la informacion codificada.
    info = urllib.request.urlopen(url)
    data = info.read().decode()

    # try-except - Obtenemos un diccionario con los elementos especificos de la API
    try:
        js = json.loads(data)
    except:
        js = None

    # Comprobamos que el status del json obtenido sea correcto
    if not js or 'status' not in js or js['status'] != 'OK':
        print('===FALLO EN LA RECUPERACION===')
        print(data)
        continue

    # Por ultimo, mostramos la Latitud y Longitud de la ubicacion
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('Latitud:', lat, 'Longitud:', lng)

    ubi = js['results'][0]['formated_address']
    print('Ubicacion:', ubi)



    


    

