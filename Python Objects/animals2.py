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
        

if __name__ == '__main__':
    # Creacion de objetos de tipo PartyAnimal
    animal1 = PartyAnimal(2, 'Toby')
    animal2 = PartyAnimal(5, 'Gordo')

    # Llamamos al metodo party() de la clase para el objeto 
    animal1.edad()
    animal2.edad()
    animal1.edad()