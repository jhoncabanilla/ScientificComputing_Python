def add_time(start, duration, day=None):
    # Formato de reloj de 12 h
    # AM --> (00:00) hasta las 11:59 de la mañana
    # PM --> (12:00) hasta las 11:59 de la noche

    # Creacion de diccionarios para las conversiones correctas
    dicc = {12:12, 13: 1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11, 24:12}
    days = {"Monday": 1, "Tuesday": 2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6, "Sunday":7}
    more_days = 0

    # Procesamos la hora de inicio y la duracion
    info = start.split()
    time = info[0]
    type = info[1]

    act_hour = int(time.split(':')[0])
    act_min = int(time.split(':')[1])

    # Duracion
    plus_hour = int(duration.split(':')[0])
    plus_min = int(duration.split(':')[1])


    # Procesamos la nueva hora
    # >> La hora de duracion puede ser cualquier numero entero
    # >> En cambio, los minutos tienes que ser menores que 60
    if plus_min > 60:
        return "Error: Minutes in duration time have to be less than 60"

    new_hour = act_hour + plus_hour
    new_min = act_min + plus_min

    # Comprobamos que las horas y min sean menores que 60 y en caso contrario realizamos los ajustes oportunos
    if new_min >= 60:
        new_hour += new_min // 60
        new_min = new_min % 60

    if new_hour >= 24:
        more_days += (new_hour // 24)
        new_hour = new_hour % 24

    # Conversion de las horas en funcion del tipo
    if type == 'AM':
        #AM --> (00:00) hasta las 11:59 de la mañana
        if new_hour >= 12:
            new_hour = dicc[new_hour]
            type = "PM"

    else:
        # El cambio de PM a AM significa +1 dia
        if new_hour >= 12:
            new_hour = dicc[new_hour]
            type = "AM"
            more_days += (new_hour // 24) + 1

    # Concatenamos la hora y le damos el formato original
    output = str(new_hour) + ":" + f"{new_min:02}" + " " + type

    # Comprobamos si se incluye el parametro del dia de la semana
    if day is not None:
        # Convertimos el dia en cuestion a minuscula al igual que las claves del diccionario para manejar el case-insensitive y comprobamos
        # que sea un dia valido
        if day.lower() in [key.lower() for key in days]:
            act_day = days[day.lower().capitalize()]
        else:
            return "Error: Insert a valid day"

        if more_days >= 1:
            # Para calcular el nuevo dia obtengo la key a partir del value de la siguiente manera:
            act_day += more_days
            final_day = list(days.keys())[list(days.values()).index(act_day if act_day <=7 else act_day%7)]
            # Realizamos la comprobacion del numero de dias extra para mostrar el msg correcto
            if more_days > 1:
                text = ", " + final_day + " ("+str(more_days)+" days later)"
            else:
                text = ", " + final_day + " (next day)"
        else:
            text = ", " + day

        output = output + text
        
    else:
        # No hay dia de comienzo
        if more_days > 1:
            text = " (" + str(more_days) + " days later)"
            output = output + text
        elif more_days == 1:
            text = " (next day)"
            output = output + text
        else:
            pass

    return output

def main():
    print(add_time("2:59 AM", "24:00", "saturDay"))

if __name__ == '__main__':
    main()