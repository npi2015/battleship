import numpy as np


def input_barco(tamanio):
    columnas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    filas = list(map(str, list(range(1, 11))))
    nseo = ['N', 'S', 'E', 'O']

    print(f'\nIntroduce un barco de tamaño {tamanio}')
    while True:
        x_user = input('Introduce la columna, valores posibles A hasta J: ')
        x_user = x_user.strip().upper()
        if x_user.strip() in columnas:
            break
        else:
            print(f'{x_user} no es un valor válido')

    while True:
        y_user = input('Introduce la fila, números posibles del 1 al 10: ')
        if y_user.strip() in filas:
            break
        else:
            print(f'{y_user} no es un número válido')

    while True:
        orientacion_user = input('Introduce la orientación del barco, valores posibles N,S,E,O: ')
        orientacion_user = orientacion_user.strip().upper()
        if orientacion_user in nseo:
            break
        else:
            print(f'{orientacion_user} no es una orientación válida')



    return int(y_user)-1, columnas[x_user], orientacion_user



def pintar_barco(tamanio, tablero, orientacion, y, x):
    '''
    Función que verifica si se puede pintar el barco y lo pinta
    :param tamanio: tamaño del barco a pintar
    :param orientacion: en qué dirección se pinta el barco a partir del punto inicial
    :param y: fila del punto inicial a partir del cual pintar el barco
    :param x: columna del punto inicial a partir del cual pintar el barco
    :return: True en caso de se haya podido pintar el barco en la orientación y coordinadas dadas.
             False en caso contrario.
    '''

    ancho = tablero.shape[0]
    alto = tablero.shape[1]

    if (orientacion == 'N') and (y >= alto-tamanio-1):
        if np.all(tablero[y-tamanio+1:y+1, x] == ' '):
            tablero[y-tamanio+1:y+1, x] = str(tamanio)
            return True

    elif (orientacion == 'S') and (y <= alto-tamanio):
        if np.all(tablero[y:y+tamanio, x] == ' '):
            tablero[y:y+tamanio, x] = str(tamanio)
            return True

    elif (orientacion == 'E') and (x <= ancho-tamanio):
        if np.all(tablero[y, x:x+tamanio] == ' '):
            tablero[y, x:x+tamanio] = str(tamanio)
            return True

    elif (orientacion == 'O') and (x >= tamanio-1):
        if np.all(tablero[y, x-tamanio+1:x+1] == ' '):
            tablero[y, x-tamanio+1:x+1] = str(tamanio)
            return True
    else:
        return False


def posicionar_barco_aleatorio(tablero, tamanio):
    '''
    Función que genera coordenadas y orientación aleatorias y llama a la función pinta_barco para que verifique si se
    puede pintar con esas variables y lo pinte en caso positivo

    :param tamanio: Tamaño del barco a pintar
    '''

    ancho = tablero.shape[0]
    alto = tablero.shape[1]

    barco_pintado = False

    while not barco_pintado:
        nseo = {1: 'N', 2: 'S', 3: 'E', 4: 'O'}
        orientacion = nseo[np.random.randint(1, 5)]

        y, x = np.random.randint(alto), np.random.randint(ancho)

        barco_pintado = pintar_barco(tamanio, tablero, orientacion, y, x)
        if barco_pintado:
            break


def posicionar_barco_usuario(tablero, tamanio):
    '''
    Función que llama a input_barco para recoger coordenadas y orientación del barco y llama a la función pinta_barco_usuario
    para que verifique si se puede pintar con esas variables y lo pinte en caso positivo. En caso de que la variable
    aleatorio que devuelve input_barco() sea True se llamará a la función pinta_barco_aleatorio

    :param tamanio: Tamaño del barco a pintar
    '''

    ancho = tablero.shape[0]
    alto = tablero.shape[1]

    barco_pintado = False

    while not barco_pintado:

        y, x, orientacion = input_barco(tamanio)

        barco_pintado = pintar_barco(tamanio, tablero, orientacion, y, x)
        if barco_pintado:
            break
        else:
            print(f'En la posicion {x}{y} con orientación {orientacion} no se puede colocar un barco de tamaño {tamanio}')
            print('Vuelve a introducir otra localización')





def crea_tablero_aleatorio(ancho, alto):
    tablero = np.full((alto, ancho), ' ')

    barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for barco in barcos:
        posicionar_barco_aleatorio(tablero, barco)

    return tablero


def crea_tablero_usuario(ancho, alto):

    print('\nCada tablero tiene 1 barco de tamaño 4, 2 barcos de tamaño 3, 3 barcos de tamaño 2 y 4 barcos de tamaño 1\n')
    tablero = np.full((alto, ancho), ' ')
    barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    aleatorio_user = input('¿Quieres que los siguientes barcos se posicionen aleatoriamente? (Y): ')
    if aleatorio_user.strip().upper() == 'Y':
        aleatorio = True
    else:
        aleatorio = False



    for barco in barcos:
        if not aleatorio:
            posicionar_barco_usuario(tablero, barco)

            aleatorio_user = input('¿Quieres que los siguientes barcos se posicionen aleatoriamente? (Y): ')

            if aleatorio_user.strip().upper() == 'Y':
                aleatorio = True

        else:
            posicionar_barco_aleatorio(tablero, barco)

    return tablero
