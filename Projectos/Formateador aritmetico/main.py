def arithmetic_arranger(problems, show=False): 
        # CHECK NUMBER OF PROBLEMS
        if len(problems) > 5:
            return ("Error: Too many problems")
        
        arranged_problems = ""
        sum = ""
                
        for i in range (len(problems)):
            elements = problems[i].split(' ')
            firstOP = elements[0]
            op = elements[1]
            secondOP = elements[2]

            # CHECK OPERATOR
            if op != '+' and op != '-':
                return ("Error: Operator must be '+' or '-'")

            # CHECK IF OPERANDs ONLY CONTAIN DIGITS
            if not firstOP.isdigit() or not secondOP.isdigit():
                return ("Error: Numbers must only contain digits")
                
            # CHECK OPERAND WIDTH
            if int(firstOP) > 9999 or int(secondOP) > 9999:
                return ("Error: Numbers cannot be more than four digits")
            
            "La anchura de cada problema debe corresponderse a la suma del operador mas largo +1 de un espacio +1 del operador"
            length = len(firstOP) if int(firstOP) > int(secondOP) else len(secondOP)
            width = length + 1 + 1

            # De esta manera conseguimos escribir cada operando alineado a la derecha con width ya calculado
            if i != len(problems)-1:
                arranged_problems = arranged_problems + "{n:>{w}}".format(n=firstOP, w=width) + "    "
            else:
                arranged_problems = arranged_problems + "{n:>{w}}".format(n=firstOP, w=width) + "\n"
            
            
            # Parte del operador y del segundo operando.
            # El operador lo ponemos en la izquierda de la cadena con :<1 y para colocar el segundo operando a la derecha del ancho del texto
            # usamos :>{w}, siendo w la anchura menos 1 para cuadrarlo de forma adecuada.

            if i != len(problems)-1:
                arranged_problems = arranged_problems + "{n:<1}{n2:>{w}}".format(n=op, n2=secondOP, w=width-1) + "    "
            else:
                arranged_problems = arranged_problems + "{n:<1}{n2:>{w}}".format(n=op, n2=secondOP, w=width-1) + "\n"
            

            # Parte de los guiones
            if i != len(problems)-1:
                arranged_problems = arranged_problems + ('-' * width) + "    "
            else:
                arranged_problems = arranged_problems + ('-' * width) + "\n"   

            # Comprobamos el segundo argumento para realizar o no las operaciones
            if show:
                # Comprobamos el operador
                if op == '+':  
                    value = str(int(firstOP) + int(secondOP))
                else:
                    value = str(int(firstOP) - int(secondOP))

                if i != len(problems)-1:
                    sum = sum + "{n:>{w}}".format(n=value, w=width) + "    "
                else:
                    sum = sum + "{n:>{w}}".format(n=value, w=width) + "\n"

        # Mostramos la cadena con o sin los resultados
        if show:
            # Imprimimos finalmente el resultado en una unica linea como es pedido
            arranged_problems = arranged_problems + sum
            output = str.join(" ", arranged_problems.splitlines())
            return output
        else:
            output = str.join(" ", arranged_problems.splitlines())
            return output

print(arithmetic_arranger(["3801 - 2", "123 + 49"], True))

expected_output = '  3801      123\n-    2    +  49\n------    -----'