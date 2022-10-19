import math
from tkinter import W


class Category:
    # Atributo de la clase
    ledger = []
    name = ""
    funds = 0
    gastos = 0

    # Constructor
    def __init__(self, name):
        self.name = name

    # deposit() method - Este metodo agrega un objeto a la lista ledger
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

        # Establecemos los fondos de la categoria
        self.funds = amount

    # withdraw() method - Este metodo agrega un objeto a la lista ledger pero con la cantidad negativa
    # Antes de añadir a ledger hay que comprobar que queden suficientes fondos
    def withdraw(self, amount, description=""):
        # Comprobamos si hay suficientes fondos
        if self.check_funds:
            self.ledger.append({"amount": -amount, "description": description})
            self.funds -= amount
            self.gastos += amount
            return True
        else:
            return False

    # get_balance() method - Este metodo devuelve el balance actual basado en los depositos y en los withdraw("gastos")
    def get_balance(self):
        return self.funds

    # clothing = Category("Clothing") ---  food.transfer(50, clothing)
    def transfer(self, amount, budget_category):
        if self.check_funds:
            # Primero añadimos al ledger el withdraw con la descripcion requerida y despues invocamos al metodo deposit de la otra categoria
            desc = "Transfer to " + budget_category.name
            self.withdraw(amount, desc)

            desc = "Transfer from "+ budget_category.name
            budget_category.deposit(amount, desc)
            return True
        else: 
            return False

    def get_ledger(self):
        return self.ledger


    # check_funds() method - Metodo que comprueba si hay suficientes fondos
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    # __str__() method - Metodo utilizado para imprimir el objeto en el formato pedido
    def __str__(self):
        leng = 30 - len(self.name)
        first = ('*' * int(leng/2) ) + str(self.name) + ('*' * int(leng/2) )
        # Imprimimos los elemetos del ledger de cada categoria
        second = ""
        for item in self.ledger:
            cant = "%.2f" % item['amount']
            second = second + '{:<23}'.format(item['description'])[:23] + '{:>7}'.format(cant)[:7] + "\n"

        third = "Total: " + str(self.funds)

        output = first + "\n" + second + third

        return output



def create_spend_chart(categories):
    # categories = [Food, Clothing]
    dicc = {}
    width = 1+ len(categories)*3
    for item in categories:
        dicc[item.name] = int(item.gastos)

    top = 100
    output = ""

    # Obtenemos una lista con los valores redondeados hacia el multiple de 10 menor
    perc = []
    for x in list(dicc.values()):
        rounded = math.floor(x / 10) * 10
        if rounded > 100:
            perc.append(100)
        else:
            perc.append(rounded) 

    #[70, 30, 20]
    #[20, 100, 0] <-----

    print(perc)
    print("width=", width)

    for i in range(11):
        val = str(top) + "|"

        if top in perc:
            output = output + '{:>4}'.format(val)[:4]
            # Comprobar para que categorias hay que marcar el valor
            for i in range(len(categories)): # 0-1-2  ---- 2-5-8
                if perc[i] == top:
                    # Simulamos un switch para obtener la posicion indicada
                    if i == 0:
                        posi = 2
                        output += '{n:>{w}}'.format(n='o', w=posi)[:width]
                    elif i == 1:
                        posi = 5
                        output += '{n:>{w}}'.format(n='o', w=posi-2)[:width]
                    elif i == 2:
                        posi = 8
                        output += '{n:>{w}}'.format(n='o', w=posi-5)[:width]
                    else:
                        posi = 11
                        output += '{n:>{w}}'.format(n='o', w=posi-8)[:width]
            output += "\n"
        else:
            output = output + '{:>4}'.format(val)[:4] + "\n"
        top -= 10



    output = output + '{:>14}'.format("-" * width) + "\n"

    # Por ultimo, mostramos los nombres de cada categoria de forma vertical
    line = ""
    nombres = ""
    claves = list(dicc.keys())
    num = len(claves)
    # Obtenemos la longitud del string mas extenso de la lista
    max_len = len(max((claves), key=len))

    # Añadimos espacios en blanco a los strings que tengan menor longitud que la maxima
    for item in claves:
        pos = claves.index(item)
        if len(item) < max_len:
            while len(item) < max_len:
                item += " "
            claves[pos] = item

    # Vamos añadiendo las mismas posiciones de cada nombre de categoria al string nombrado 'nombres'
    for index in range(max_len):
        for j in range(num):
            line += claves[j][index] + "  "
        nombres += '{:>14}'.format(line) + "\n"
        line = ""

    output += nombres

    return output


def main():
    food = Category("Food")
    clothing = Category("Clothing")
    business = Category("Business")
    auto = Category("Auto")

    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(100, "restaurant and more food for dessert")

    clothing.deposit(1000, "initial deposit")
    clothing.withdraw(10.15)
    clothing.withdraw(100)

    business.deposit(1000, "initial deposit")
    business.withdraw(10.15)
    business.withdraw(100)

    auto.deposit(1000, "initial deposit")
    auto.withdraw(10.15)
    auto.withdraw(100)

    """ food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    #print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)"""

    #print(food)
    #print(clothing)

    #expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    #print(expected)

    print(create_spend_chart([food, clothing, business]))


if __name__ == "__main__":
    main()
