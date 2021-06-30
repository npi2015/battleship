"File for classes and objects"
from constantes import tablero
import numpy as np
class Tablero():
    def __init__(self, tablero):
        self.tablero = tablero

class Barcos:
    def __init__(self, orientacion):
        self.portaaviones = 4
        self.acorazado = 3
        self.fragata = 2
        self.submarino = 1
        if orientacion in ["horizontal", "vertical"]:
            self.orientacion = orientacion
        else:
            raise ValueError("La orientacion tiene que ser horizontal o vertical")
    def colocar_barcos_horizontal(self, row, starting_column):
        if starting_column + self.portaaviones > 10:
            raise IndexError("El barco se sale del tablero")
        elif not np.all(tablero[row, starting_column: starting_column + self.portaaviones], 0):
            tablero[row, starting_column: starting_column + self.portaaviones] = 1
        else:
            raise IndexError("Ya hay un barco en esa posicion")
    def colocar_barcos_vertical(self, starting_row, column):
        if starting_column + self.portaaviones > 10:
            raise IndexError("El barco se sale del tablero")
        elif not np.all(tablero[starting_row: starting_row + self.submarino, column], 0):
            tablero[starting_row: starting_row + self.submarino, column] = 1
        else:
           raise IndexError("Ya hay un barco en esa posicion")
    def detectar_impacto(self, coordenada_x, coordenada_y):
        if tablero[coordenada_x, coordenada_y] == 1:
            print("Has golpeado un barco")
            tablero[coordenada_x, coordenada_y] = 2
        else:
            print("Has fallado")
            tablero[coordenada_x, coordenada_y] = "o"

Barcos("vertical").colocar_barcos_horizontal(8,4)
Barcos("vertical").detectar_impacto(8,4)

print(tablero)

# TODO: crear array con caracteres, usar x para impactos y o para fallos

