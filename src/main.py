from NoClasses import *

juego_en_progreso = True
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tablero_maquina =  fase_preliminar(crear_tablero(), maquina = True)
    tablero_usuario = fase_preliminar(crear_tablero(), maquina = True)
    print("\n Tablero del usuario\n")
    print(tablero_usuario)
    while juego_en_progreso:
        # Turno del usuario
        tablero_usuario_golpes = disparar(tablero_maquina, np.random.randint(0, 9), np.random.randint(0, 9))
        # Checkear si hemos hundido todos los barcos
        if not np.any(np.isin(tablero_usuario, ["1", "2", "3", "4"])):
            print("Ha ganado la maquina")
            print("\n Tablero de la maquina\n")
            print(tablero_maquina)
            print("\n Tu tablero\n")
            print(tablero_usuario)
            juego_en_progreso = False

        # Imprimimos los golpes que ha dado el usuario
        print("\n Golpes dados al enemigo\n")
        print(tablero_usuario_golpes)
        print("\n Golpes recibidos\n")
        print(tablero_usuario)


        #Turno de la maquina
        tablero_maquina_golpes = disparar(tablero_usuario, np.random.randint(0, 9), np.random.randint(0, 9))

        # Miramos si ha ganado la maquina
        if not np.any(np.isin(tablero_maquina, ["1", "2", "3", "4"])):
            print("Has ganado!")
            print("\n Tu tablero\n")
            print(tablero_usuario)
            print("\n El tablero del enemigo\n")
            print(tablero_maquina)
            juego_en_progreso = False

# TODO: implementar que el jugador pueda meter las coordenadas a mano