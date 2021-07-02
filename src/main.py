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
        coordenadas = input("¿A qué coordenadas quieres disparar?(formato: A7) ")
        coordenada_y, coordenada_x = valid_input(coordenadas)
        tablero_usuario_golpes = disparar(tablero_maquina, coordenada_x, coordenada_y)

        # Checkear si hemos hundido todos los barcos -> Jugador gana
        if not np.any(np.isin(tablero_usuario, ["1", "2", "3", "4"])):
            print("Ha ganado la maquina")
            pinta_1_tablero(tablero_maquina, "Tablero de la maquina")
            pinta_1_tablero(tablero_usuario, "        Tu tablero")
            juego_en_progreso = False
        else:
            # Imprimimos los golpes que ha dado el usuario
            pinta_1_tablero(tablero_usuario_golpes, "Golpes dados al enemigo")
            print("\n TURNO DE LA MÁQUINA")
            time.sleep(5)
            #Turno de la maquina
            tablero_maquina_golpes = disparar(tablero_usuario, np.random.randint(0, 9), np.random.randint(0, 9), random = True)

            # Imprimimos los golpes recibidos por el usuario
            # pinta_1_tablero(tablero_usuario, "        Tu tablero")
            print("\n TU TURNO")
            pinta_2_tableros(tablero_usuario, tablero_usuario_golpes, '        Tu tablero', '    Impactos en el contario')

            # Miramos si ha ganado la maquina
            if not np.any(np.isin(tablero_maquina, ["1", "2", "3", "4"])):
                print("Has ganado!")
                pinta_1_tablero(tablero_usuario, "        Tu tablero")
                pinta_1_tablero(tablero_maquina, "Tablero del enemigo")
                juego_en_progreso = False

print("ACABADO")
# TODO:  implementar que el jugador pueda meter las coordenadas a mano