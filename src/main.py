from functions import *
from tablero import crea_tablero_usuario, crea_tablero_aleatorio
import numpy as np
import time

juego_en_progreso = True
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("""
  _    _                 _           _           __ _       _        
 | |  | |               | (_)       | |         / _| |     | |       
 | |__| |_   _ _ __   __| |_ _ __   | | __ _   | |_| | ___ | |_ __ _ 
 |  __  | | | | '_ \ / _` | | '__|  | |/ _` |  |  _| |/ _ \| __/ _` |
 | |  | | |_| | | | | (_| | | |     | | (_| |  | | | | (_) | || (_| |
 |_|  |_|\__,_|_| |_|\__,_|_|_|     |_|\__,_|  |_| |_|\___/ \__\__,_|
                                                                    
    """)
    tablero_maquina = crea_tablero_aleatorio(10, 10)
    tablero_usuario = crea_tablero_usuario(10, 10)
    pinta_1_tablero(tablero_usuario, "        Tu tablero")
    while juego_en_progreso:
        # Turno del usuario
        coordenadas = input("¿A qué coordenadas quieres disparar?(formato: A7) ")
        coordenada_y, coordenada_x = valid_input(coordenadas)
        tablero_usuario_golpes = disparar(tablero_maquina, coordenada_x, coordenada_y)

        # Miramos si ha ganado el usuario
        if not np.any(np.isin(tablero_maquina, ["1", "2", "3", "4"])):
            print("Has ganado!")
            pinta_2_tableros(tablero_usuario, tablero_maquina, '        Tu tablero', '    Tablero de la máquina')
            juego_en_progreso = False

        else:
            # Imprimimos los golpes que ha dado el usuario
            pinta_1_tablero(tablero_usuario_golpes, "Golpes dados al enemigo")
            print("\n TURNO DE LA MÁQUINA")
            time.sleep(2)
            #Turno de la maquina
            tablero_maquina_golpes = disparar(tablero_usuario, np.random.randint(0, 9), np.random.randint(0, 9), random = True)

            # Imprimimos los golpes recibidos por el usuario
            # pinta_1_tablero(tablero_usuario, "        Tu tablero")
            print("\n TU TURNO")
            pinta_2_tableros(tablero_usuario, tablero_usuario_golpes, '          Tu tablero', '   Impactos al contario')

            # Checkear si todos nuestros barcos estan hundidos -> maquina gana
            if not np.any(np.isin(tablero_usuario, ["1", "2", "3", "4"])):
                print("Ha ganado la maquina")
                pinta_2_tableros(tablero_maquina, tablero_usuario, "    Tablero de la máquina", '    Tu tablero')
                juego_en_progreso = False

print("ACABADO")
# TODO:  implementar que el jugador pueda meter las coordenadas a mano