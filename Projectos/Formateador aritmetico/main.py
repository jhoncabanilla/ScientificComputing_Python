def arithmetic_arranger(problems, show=False): 
    # Comprobamos el numero de problemas
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Creamos cadenas vacias las cuales iremos rellenando con los valores de los problemas
    # >> up : contendra los primeros operandos de cada problema
    # >> down: contendra los operadores y los segundos operandos de cada problema
    # >> dashes: contendra los guiones correspondientes de cada problema
    # >> result: contendra los resultados de cada problema
    up = ""
    down = ""
    dashes = ""
    result = ""

    for i in range (len(problems)):
        element = problems[i].split(' ')
        # Obtenemos los elementos necesarios
        firstOP = element[0]
        op = element[1]
        secondOP = element[2]
        
        # Pasamos a realizar las comprobaciones restantes
        # Chequeo del operador
        if op != '+' and op != '-':
            return "Error: Operator must be '+' or '-'."
        # Comprobamos que los operadores contengan solo digitos - Se podria utilizar RegExp tambien
        elif not firstOP.isdigit() or not secondOP.isdigit():
            return "Error: Numbers must only contain digits."
        # Comprobamos que los operadores no tengan mas de 4 digitos
        elif int(firstOP) > 9999 or int(secondOP) > 9999:
            return "Error: Numbers cannot be more than four digits."
        else:
            # Una realizadas las comprobaciones continuamos calculando el ancho de cada problema
            # La anchura de cada problema debe corresponderse a la suma del operador mas largo +1 de un espacio +1 del operador
            length = len(firstOP) if int(firstOP) > int(secondOP) else len(secondOP)
            width = length + 1 + 1

            # Las siguiente estructura la utilizo para añadir los espacios en blanco al final y para el ultimo problema lo añado ya sin los espacios
            # Para alinear utilizo format. Para alinear el texto a la derecha uso :> y para la izquierda :<. W hace referencia al espacio disponible
            # que es el ancho de cada problema. Por ultimo, para alinear a la izquierda, utilo el valor 1 para colocarlo en la primera posicion del string.
            if i != len(problems)-1:
                up = up + "{n:>{w}}".format(n=firstOP, w=width) + "    "
                down = down + "{n:<1}{n2:>{w}}".format(n=op, n2=secondOP, w=width-1) + "    "
                dashes = dashes + ('-' * width) + "    "
            else:
                up = up + "{n:>{w}}".format(n=firstOP, w=width)
                down = down + "{n:<1}{n2:>{w}}".format(n=op, n2=secondOP, w=width-1)
                dashes = dashes + ('-' * width)

            # Procedemos a realizar las operaciones en funcion del operador en cuestion y almacenamos los resultados en el string correspondiente.
            if op == '+':
                value = str(int(firstOP) + int(secondOP))
            else:
                value = str(int(firstOP) - int(secondOP))

            if i != len(problems)-1:
                result = result + "{n:>{w}}".format(n=value, w=width) + "    "
            else:
                result = result + "{n:>{w}}".format(n=value, w=width)

    # Por ultimo, comprobamos el segundo argumento para mostrar o no los resultados
    if show:
        arranged_problems = up + "\n" + down + "\n" + dashes + "\n" + result
    else:
        arranged_problems = up + "\n" + down + "\n" + dashes

    return arranged_problems

def main():
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

if __name__ == '__main__':
    main()