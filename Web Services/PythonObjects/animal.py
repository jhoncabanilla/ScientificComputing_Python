class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print("x vale:", self.x)
        
if __name__ == '__main__':
    # Creacion de objetos de tipo PartyAnimal
    animal1 = PartyAnimal()
    animal2 = PartyAnimal()

    # Llamamos al metodo party() de la clase para el objeto 
    animal1.party()
    animal1.party()
    animal1.party()
    animal2.party()

    # El comando dir muestra los metodos que el objeto implementa de la clase
    print(dir(animal1))