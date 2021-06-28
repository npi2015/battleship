"File for classes and objects"

class tablero():
    def __init__(self, tablero):
        self.tablero = tablero

class barcos():
    def __init__(self):
        self.portaaviones = 4
        self.acorazado = 3
        self.buque = 2
        self.submarino = 1
    def colocar_barcos_horizontal(self, row, starting_column):
        if starting_column + self.portaaviones > 10:
            print("El barco se sale del tablero")
        elif not np.all(tablero[row, starting_column: starting_column + self.portaaviones],0):
            tablero[row, starting_column: starting_column + self.portaaviones] = 1
        else:
            print("Ya hay un barco en esa posicion")
    def colocar_barcos_vertical(self, starting_row, column):
        if starting_column + self.portaaviones > 10:
            print("El barco se sale del tablero")
        elif not np.all(tablero[starting_row: starting_row + self.submarino, column], 0):
            tablero[starting_row: starting_row + self.submarino, column] = 1
        else:
           print("Ya hay un barco en esa posicion")
