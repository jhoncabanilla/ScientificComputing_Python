def arithmetic_arranger(problems, show=False): 
        # CHECK NUMBER OF PROBLEMS
        if len(problems) > 5:
            return "Error: Too many problems."
        
        up = ""
        down = ""
        dashes = ""
        result = ""

        for i in range (len(problems)):
            element = problems[i].split(' ')
            firstOP = element[0]
            op = element[1]
            secondOP = element[2]
           
            # CHECK OPERATOR
            if op != '+' and op != '-':
                return "Error: Operator must be '+' or '-'."
            # CHECK IF OPERANDs ONLY CONTAIN DIGITS
            elif not firstOP.isdigit() or not secondOP.isdigit():
                return "Error: Numbers must only contain digits."
            # CHECK OPERAND WIDTH
            elif int(firstOP) > 9999 or int(secondOP) > 9999:
                return "Error: Numbers cannot be more than four digits."
            else:
                "La anchura de cada problema debe corresponderse a la suma del operador mas largo +1 de un espacio +1 del operador"
                length = len(firstOP) if int(firstOP) > int(secondOP) else len(secondOP)
                width = length + 1 + 1

            # De esta manera conseguimos escribir el primer operando alineado a la derecha con width ya calculado
            if i != len(problems)-1:
                up = up + "{n:>{w}}".format(n=firstOP, w=width) + "    "
                down = down + "{n:<1}{n2:>{w}}".format(n=op, n2=secondOP, w=width-1) + "    "
                dashes = dashes + ('-' * width) + "    "
            else:
                up = up + "{n:>{w}}".format(n=firstOP, w=width)
                down = down + "{n:<1}{n2:>{w}}".format(n=op, n2=secondOP, w=width-1)
                dashes = dashes + ('-' * width)

            # Procedemos a almacenar el operador, segundo operando y resultamos de la suma/resta
            if op == '+':
                value = str(int(firstOP) + int(secondOP))
            else:
                value = str(int(firstOP) - int(secondOP))

            if i != len(problems)-1:
                result = result + "{n:>{w}}".format(n=value, w=width) + "    "
            else:
                result = result + "{n:>{w}}".format(n=value, w=width)

        # Comprobamos el segundo argumento para realizar o no las operaciones
        if show:
            arranged_problems = up + "\n" + down + "\n" + dashes + "\n" + result
        else:
            arranged_problems = up + "\n" + down + "\n" + dashes

        return arranged_problems



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

expected_output = '  3801      123\n-    2    +  49\n------    -----'
expected_output ='   3801      123 -   2    +  49 ------    -----'