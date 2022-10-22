import copy
import random

# Consider using the modules imported above.

class Hat:
    # Constructor
    # Como el numero de argumentos que se pasa es variable, utilizamos **kwargs lo cual nos crea un diccionario con los datos clave
    # Esta variable diccionario tiene el nombre kwargs
    def __init__(self, **kwargs):
        self.contents = []
        self.set_contents(kwargs)

    # Metodo mediante el cual construimos la lista contents con cada una de las claves del diccionario
    def set_contents(self, kwargs):
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    # Metodo que extrae un numero x de bolas de forma aleatoria - Retornamos una lista con las pelotas extraidas
    def draw(self, balls_draw):
        if balls_draw >= len(self.contents):
            return self.contents
        else:
            drawn_balls = []
            for i in range(balls_draw):
                # Numero aleatorio entre 0 y la longitud de la cadena contents -1 para indexar correctamente
                aleat = random.randint(0, len(self.contents)-1)
                drawn_balls.append(self.contents[aleat])
                self.contents.pop(aleat)

            return drawn_balls
            

# Como pista nos dicen que utilicemos el modulo copy, lo cual nos crea una nueva instancia independiente del objeto --> deepcopy
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    # Realizamos los n experimentos
    for i in range(num_experiments):
        # Hacemos la copia del hat para cada experimento
        copy_hat = copy.deepcopy(hat)
        drawn = copy_hat.draw(num_balls_drawn)

        for key, value in expected_balls.items():
            count = drawn.count(key) # Numero de veces que aparece la clave en la lista de bolas extraidas
            # Si este numero de veces es mayor o igual que el valor marcado en el diccionario ponemos una variable auxiliar 'expe' a True.
            # Debemos comprobar el resto de elementos. Para el caso en el que 1 no cumpla la condicion, salimos del bucle for y nos aumentamos m
            if count >= value:
                expe = True
            else:
                expe = False
                break
        if expe:
            m += 1

    probability = m/num_experiments

    return probability


def main():
    random.seed(95)

    hat = Hat(blue=3,red=2,green=6)
    probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
    print("Probability:", probability)


if __name__ == '__main__':
    main()