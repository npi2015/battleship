import numpy as np
from string import ascii_uppercase


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
    print(titulo1, '\t\t ', titulo2)
    print('    ===================\t\t\t===================')
    print('   ', *list(ascii_uppercase[:10]), '\t   ', *list(ascii_uppercase[:10]))
    print('    -------------------\t\t\t-------------------')

    for i in range(10):
        print('{:2} |'.format(i+1), end="")
        print(*tablero1[i], end="")
        print('|\t', end="")
        print('{:2} |'.format(i+1), end="")
        print(*tablero2[i], end="")
        print('|')

    print('    -------------------\t\t\t-------------------')


if __name__ == '__main__':
    from tablero import crea_tablero_aleatorio

    tablero1 = crea_tablero_aleatorio(10, 10)
    tablero2 = crea_tablero_aleatorio(10, 10)

    pinta_1_tablero(tablero1, '        Tu tablero')
    pinta_2_tableros(tablero1, tablero2, '        Tu tablero', '    Impactos en el contario')