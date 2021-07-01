import numpy as np
from errors import *
import re


def disparar(tablero, coordenada_x, coordenada_y, random = False) :

    if tablero[coordenada_x, coordenada_y] in ["1", "2", "3", "4"]:
        tablero[coordenada_x, coordenada_y] = "X"
        if random is False:
            print("Impacto, puedes disparar de nuevo")
            coordenadas = input("Introduce nuevas coordenadas")
            usuario_coordenada_x, usuario_coordenada_y = valid_input(coordenadas)
            disparar(tablero, usuario_coordenada_x, usuario_coordenada_y)

        else:
            print("Impacto de la maquina")
            nueva_coordenada_x = np.random.randint(low=0, high=10)
            nueva_coordenada_y = np.random.randint(low=0, high=10)
            disparar(tablero, nueva_coordenada_x, nueva_coordenada_y, random=True)

    elif tablero[coordenada_x, coordenada_y] in ["X", "-"]:
        if random is True:
            nueva_coordenada_x = np.random.randint(low=0, high=10)
            nueva_coordenada_y = np.random.randint(low=0, high=10)
            disparar(tablero, nueva_coordenada_x, nueva_coordenada_y, random = True)

        else:
            print("Ahí ya has disparado")
            coordenadas = input("Introduce nuevas coordenadas")
            usuario_coordenada_x, usuario_coordenada_y = valid_input(coordenadas)
            disparar(tablero, usuario_coordenada_x, usuario_coordenada_y)

    else:
        tablero[coordenada_x, coordenada_y] = "-"

        if random is False:
            print("Has fallado")

        else:
            print("La maquina ha fallado")

    tablero = np.where(np.isin(tablero,["1", "2", "3", "4"]) , " ", tablero)
    return tablero


def valid_input(coordenadas):
    lista_de_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    x = re.match("^[a-jA-J][1-9]$", coordenadas.strip())
    y = re.match("^[a-jA-J]10$", coordenadas.strip())
    while x is None and y is None:
        print("Esas coordenadas no son validas")
        coordenadas = input("Por favor introduce coordenadas validas")
        x = re.match("^[a-jA-J][1-9]$", coordenadas.strip())
        y = re.match("^[a-jA-J]10$", coordenadas.strip())
    columna = lista_de_letras.index(coordenadas.strip()[0])
    if x:
        fila = int(coordenadas.strip()[1]) - 1
    if y:
        fila = 9
    return columna, fila



# TODO: prettify printed tablero
# TODO: add loops for actual playability
# FIX: submarines cannot be placed facing outwards in the edges
