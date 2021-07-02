from functions import disparar, valid_input
from tablero import crea_tablero_usuario, crea_tablero_aleatorio
from visualizacion import *
import numpy as np
import time

juego_en_progreso = True
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tablero_maquina = crea_tablero_aleatorio(10, 10)
    tablero_usuario = crea_tablero_usuario(10, 10)
    pinta_1_tablero(tablero_usuario, "Tablero del usuario")
    while juego_en_progreso:
        # Turno del usuario
        coordenadas = input("A que coordenadas quieres disparar")
        coordenada_x, coordenada_y = valid_input(coordenadas)
        tablero_usuario_golpes = disparar(tablero_maquina, coordenada_x, coordenada_y)
        # Checkear si hemos hundido todos los barcos
        if not np.any(np.isin(tablero_usuario, ["1", "2", "3", "4"])):
            print("Ha ganado la maquina")
            pinta_1_tablero(tablero_maquina, "Tablero de la maquina")
            pinta_1_tablero(tablero_usuario, "Tu tablero")
            break

        # Imprimimos los golpes que ha dado el usuario
        pinta_1_tablero(tablero_usuario_golpes, "Golpes dados al enemigo")
        print("\n Turno de la maquina")
        time.sleep(5)
        #Turno de la maquina
        tablero_maquina_golpes = disparar(tablero_usuario, np.random.randint(0, 9), np.random.randint(0, 9), random = True)

        # Imprimimos los golpes recibidos por el usuario
        pinta_1_tablero(tablero_usuario, "Golpes recibidos")

        # Miramos si ha ganado la maquina
        if not np.any(np.isin(tablero_maquina, ["1", "2", "3", "4"])):
            print("Has ganado!")
            pinta_1_tablero(tablero_usuario, "Tu tablero")
            pinta_1_tablero(tablero_maquina, "Tablero del enemigo")
            juego_en_progreso = False

print("ACABADO")
# TODO:  implementar que el jugador pueda meter las coordenadas a mano