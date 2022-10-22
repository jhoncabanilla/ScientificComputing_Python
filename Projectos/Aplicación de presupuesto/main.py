import math


class Category:
    # Constructor
    def __init__(self, name):
        # Atributo de la clase
        self.name = name
        self.ledger = []
        self.funds = 0
        self.gastos = 0
        self.marked = False

    # Este metodo agrega un objeto a la lista ledger, indicando el ingreso y la descripcion
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

        # Establecemos los fondos de la categoria
        self.funds = amount

    # Este metodo devuelve el balance actual basado en los depositos y en los withdraw("gastos")
    def get_balance(self):
        return self.funds
    
    # Metodo que comprueba si hay suficientes fondos
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    # Este metodo agrega un objeto a la lista ledger pero con la cantidad negativa
    # Antes de añadir a ledger hay que comprobar que queden suficientes fondos
    def withdraw(self, amount, description=""):
        # Comprobamos si hay suficientes fondos
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.funds -= amount
            self.gastos += amount
            return True
        else:
            return False

    # Metodo que realiza una transferencia a la categoria indicada
    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            # Primero añadimos al ledger el withdraw con la descripcion requerida y despues invocamos al metodo deposit de la otra categoria
            desc = "Transfer to " + budget_category.name
            self.withdraw(amount, desc)

            desc = "Transfer from "+ self.name
            budget_category.deposit(amount, desc)
            return True
        else: 
            return False

    # _Metodo utilizado para imprimir el objeto en el formato pedido
    def __str__(self):
        leng = 30 - len(self.name)
        first = ('*' * int(leng/2) ) + str(self.name) + ('*' * int(leng/2) )
        # Imprimimos los elemetos del ledger de cada categoria
        second = ""
        for item in self.ledger:
            cant = "%.2f" % item['amount']
            second = second + '{:<23}'.format(item['description'])[:23] + '{:>7}'.format(cant)[:7] + "\n"

        third = "Total: " + "%.2f" % self.funds

        output = first + "\n" + second + third

        return output


def create_spend_chart(categories):   
    # Calculamos el ancho de la parte de los porcentajes
    width = 1+ len(categories)*3

    # Calculamos el gasto total a partir del withdraw de cada categoria
    gastos_totales = 0
    for item in categories:
        gastos_totales += item.gastos

    # Tenemos que redondear los gastos de cada categoria hacia abajo, al entero mas cercano
    dicc = {}
    for item in categories:
        rounded = math.floor((item.gastos/gastos_totales)*10) * 10 # Multiplicamos para hacerlo multiple de 10 para luego representarlo
        if rounded > 100:
            dicc[item] = 100
        else:
            dicc[item] = rounded

    top = 100
    output = "Percentage spent by category\n"
    # Creamos este String de espaciado igual al ancho para representar los caracteres de forma correcta
    derecha = ' ' * width

    for i in range(11):
        val = str(top) + "|"
        lista = list(derecha)
        # Marcas laterales izquierdas iniciales
        output = output + '{:>4}'.format(val)[:4]

        # Marcamos el porcentaje con 'o'
        for key, value in dicc.items():
            if value >= top:
                # Necesitamos el indice que ocupa cada key
                pos = list(dicc.keys()).index(key)
                # Segun la posicion obtenida, colocamos 'o' en dicha posicion y luego realizamos un join para darle la forma correcta
                lista[(pos + (pos*2+1) )] = 'o'
                derecha = ''.join(lista)
        output += derecha + "\n"
        top -= 10

    # Procedemos a dibujar los guiones y el nombre de cada categoria
    dashes = "-" * width
    output += '{n:>{w}}'.format(n=dashes, w=width+4) + "\n"

    # Por ultimo, mostramos los nombres de cada categoria de forma vertical
    claves = [key.name for key in dicc.keys()]
    max_len = len(max((claves), key=len)) # Obtenemos la longitud del string mas extenso de la lista

    # Para mostrar los nombre de forma vertical, seguimos el mismo metodo que el utilizado para dibujar los porcentajes
    abajo = " " * width
    for i in range(max_len):
        lista = list(abajo)
        # Marcas laterales izquierdas iniciales
        output = output + '{:>4}'.format(' ')[:4]
        for j in range(len(claves)):
            # Comprobamos si llegamos a un nombre menor que el mas largo, para en ese caso no escribir el caracter correspondiente, sino un espacio en blanco
            if len(claves[j]) > i:
                lista[(j + (j*2+1) )] = claves[j][i]
                abajo = ''.join(lista)
            else:
                lista[(j + (j*2+1) )] = " "
                abajo = ''.join(lista)
                
        # Lo ultimo, compruebo si estamos en la ultima iteracion para evitar el ultimo "\n" y mostrar el resultado correcto
        if i == (max_len-1):
            output += abajo
        else:
            output += abajo + "\n"

    return output


def main():
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")

    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")

    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)

    print(create_spend_chart([business, food, entertainment]))

    
if __name__ == "__main__":
    main()