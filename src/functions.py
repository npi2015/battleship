import numpy as np
import re
from string import ascii_uppercase


def disparar(tablero, coordenada_x, coordenada_y, random = False) :
    """Toma unas coordenadas y dispara. Tres casos se contemplan:
    1) Las coordenadas coinciden con un barco del enemigo -> La funcion se vuelve a llamar con nuevas coordenadas
    2) Las coordenadas coinciden con una posición a la que ya se ha disparado -> La función se vuelve a llamar con nuevas coordenadas
    3) Las coordenadas coinciden con una posición en la que no hay nada -> La función acaba y pasa a ser el siguiente turno

    Las coordenadas se reemplazan en el tablero del usuario o de la maquina, del cual se crea una copia para operar sobre él.
    Tras hacer las comprobaciones, todas las posiciones en las que hay números (barcos) se borran para que no se puedan ver.
    Params:
    tablero (np.array): tablero sobre el que se empieza operando. Puede ser el del usuario si dispara la máquina, o el de la máquina
             si dispara el usuario
    coordenada_x (int): columna sobre la que se dispara
    coordenada_y (int): fila sobre la que se dispara
    random (bool) {predeterminado = False}: determina si la creación de coordenadas en llamadas recursivas de la función es
                                            aleatoria para los disparos de la máquina.

    Returns:
         Un tablero con los disparos realizados, mostrando impactos y fallos
    """
    # Ha habido un impacto
    if tablero[coordenada_x, coordenada_y] in ["1", "2", "3", "4"]:
        tablero[coordenada_x, coordenada_y] = "X"
        if random is False:
            print("Impacto, puedes disparar de nuevo")
            coordenadas = input("Introduce nuevas coordenadas: ")
            usuario_coordenada_y, usuario_coordenada_x = valid_input(coordenadas)
            disparar(tablero, usuario_coordenada_x, usuario_coordenada_y)

        else:
            print("Impacto de la máquina")
            nueva_coordenada_x = np.random.randint(low=0, high=10)
            nueva_coordenada_y = np.random.randint(low=0, high=10)
            disparar(tablero, nueva_coordenada_x, nueva_coordenada_y, random=True)
    # Se dispara a una posición a la que ya se ha disparado antes
    elif tablero[coordenada_x, coordenada_y] in ["X", "-"]:
        if random is True:
            nueva_coordenada_x = np.random.randint(low=0, high=10)
            nueva_coordenada_y = np.random.randint(low=0, high=10)
            disparar(tablero, nueva_coordenada_x, nueva_coordenada_y, random = True)

        else:
            print("Ahí ya has disparado")
            coordenadas = input("Introduce nuevas coordenadas: ")
            usuario_coordenada_y, usuario_coordenada_x = valid_input(coordenadas)
            disparar(tablero, usuario_coordenada_x, usuario_coordenada_y)
    # Agua
    else:
        tablero[coordenada_x, coordenada_y] = "-"

        if random is False:
            print("Has fallado")

        else:
            print("La máquina ha fallado")

    tablero = np.where(np.isin(tablero,["1", "2", "3", "4"]) , " ", tablero)
    return tablero


def valid_input(coordenadas):
    '''Comprueba si un string son coordenadas validas. En el caso de que no lo sean, las vuelve a pedir hasta que
    se introduzcan coordenadas validas

    params:
        Coordenadas (string): las coordenadas que quiera uno meter, pueden ser lo que quieras porque la función solo
                              sale del while si es algo valida
    Returns:
        coordenada_x -> columna de la coordenada introducida por el usuario
        coordenada_y -> fila de la coordenada introducida por el usuario
    '''

    lista_de_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] # Nombres de las columnas
    # Regex para que el input sea del formato deseado, no conseguí hacerlo con una sola
    x = re.match("^[a-jA-J][1-9]$", coordenadas.strip())
    y = re.match("^[a-jA-J]10$", coordenadas.strip())
    # Si no hay un match, el objeto match devuelve None
    while x is None and y is None:
        print("Esas coordenadas no son validas")
        coordenadas = input("Por favor introduce coordenadas validas ")
        x = re.match("^[a-jA-J][1-9]$", coordenadas.strip())
        y = re.match("^[a-jA-J]10$", coordenadas.strip())
    columna = lista_de_letras.index(coordenadas.strip()[0].upper())
    # Si x o y no son None, dependiendo de que fila quiera el usario
    if x:
        fila = int(coordenadas.strip()[1]) - 1
    if y:
        fila = 9
    return columna, fila

def pinta_1_tablero(tablero, titulo):
    print(titulo)
    print('    ===================')
    print('   ', *list(ascii_uppercase[:10]))
    print('    -------------------')

    for i in range(10):
        print('{:2} |'.format(i+1), end="")
        print(*tablero[i], end="")
        print('|')

    print('    -------------------')


def pinta_2_tableros(tablero1, tablero2, titulo1, titulo2):
    print()
    print(titulo1, '     ', titulo2)
    print('    ===================       ===================')
    print('   ', *list(ascii_uppercase[:10]), '     ', *list(ascii_uppercase[:10]))
    print('    -------------------       -------------------')

    for i in range(10):
        print('{:2} |'.format(i+1), end="")
        print(*tablero1[i], end="")
        print('|  ', end="")
        print('{:2} |'.format(i+1), end="")
        print(*tablero2[i], end="")
        print('|')

    print('    -------------------       -------------------')

