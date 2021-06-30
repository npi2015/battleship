from NoClasses import *
tablero_usuario = np.full((10,10), " ")
tablero_maquina = np.full((10,10), " ")
tablero_maquina_golpes = np.full((10,10), " ")
tablero_usuario_golpes = np.full((10,10), " ")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tablero_maquina =  crear_tablero(tablero_maquina, maquina = True)
    print(tablero_maquina)
    tablero_usuario = crear_tablero(tablero_usuario, maquina = True)
    print(tablero_usuario)
    for i in range(90):
        tablero_usuario_golpes = disparar(tablero_usuario, np.random.randint(0,9), np.random.randint(0,9))
    print(tablero_usuario_golpes)
    print(tablero_usuario)

