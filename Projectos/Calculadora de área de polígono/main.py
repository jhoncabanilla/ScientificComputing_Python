# En este projecto se usara programacion orientada a objetos para crear una clase Rectangulo y una clase cuadrado
# La clase cuadrado debe ser una subclase de Rectangulo y heredar metodos y atributos
class Rectangle:
    width = 0
    height = 0

    # Constructror
    def __init__(self, width, height) -> None:
        self.set_width(width)
        self.set_height(height)

    # Setters
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # Getters
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Calculo del area del rectangulo: width * height
    def get_area(self):
        return self.width * self.height

    # Calculo del perimetro del rectangulo: 2*width + 2*height
    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    # Calculo de la diagonal del rectangulo: (width^2 + height^2)^(0.5)
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**(0.5)

    # Funcion que devuelve la forma del rectangulo usando '*'
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            shape = ""
            for i in range(self.height):
                shape += ('*' * self.width) + "\n"

            return shape

    def __str__(self) -> str:
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    # Esta funcion devuelve el numero de veces que el shape pasado podria caber en el Rectangulo o Cuadrado actual
    # >> shape: Rectangulo o Cuadrado
    def get_amount_inside(self, shape):
        amount = int(self.get_area() / shape.get_area())
        return amount

# Cuadrado hereda de la clase Rectangulo
class Square(Rectangle):

    # Constructor
    def __init__(self, side) -> None:
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side):
        super().set_height(side)
        super().set_width(side)

    def __str__(self) -> str:
        return "Square(side={})".format(self.width)


def main():
    rect = Rectangle(5, 10)
    print(rect.get_area())
    rect.set_width(3)
    print(rect.get_perimeter())
    print(rect)

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)


if __name__ == '__main__':
    main()