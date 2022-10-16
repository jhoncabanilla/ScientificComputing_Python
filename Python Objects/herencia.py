class PartyAnimal:
    # Atributos de la clase
    age = None
    name = ''
    # Constructor de la clase - Inicializa los atributos de la clase
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print("I am:", self.name)

    def edad(self):
        self.age = self.age + 2
        print("age:", self.age)


# Expreseamos la herencia poniendo la clase parent entre parentesis.
class FootballFan(PartyAnimal):
    goalScored = 0

    def score(self):
        self.goalScored = self.goalScored + 1
        print("Goals scored:", self.goalScored)
        self.edad()      

if __name__ == '__main__':
    # Creacion de objetos de tipo PartyAnimal
    animal1 = PartyAnimal(2, 'Toby')
    # Llamamos al metodo party() de la clase para el objeto 
    animal1.edad()
    animal1.edad()
 
    fan1 = FootballFan(21, 'Jimmy')
    fan1.edad()
    fan1.score()

