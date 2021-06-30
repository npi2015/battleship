import numpy as np
from errors import *

tablero_usuario = np.full((10,10), " ")
tablero_maquina = np.full((10,10), " ")
tablero_maquina_golpes = np.full((10,10), " ")
tablero_usuario_golpes = np.full((10,10), " ")
barcos = {"portaaviones" : 4, "acorazado" : 3, "fragata" : 2, "submarino" : 1}

def colocar_submarino(tablero, coordenada_inicial_x, coordenada_inicial_y):
    if tablero[coordenada_inicial_x, coordenada_inicial_y] != " ":
        raise PositionOccupiedError
    else:
        tablero[coordenada_inicial_x, coordenada_inicial_y] = "O"
    return tablero
def colocar_barco(tablero, coordenada_inicial_x, coordenada_inicial_y, orientacion, barco):
    if orientacion == "norte" and not all(
            np.where(tablero[coordenada_inicial_x: coordenada_inicial_x - barcos[barco]:-1, coordenada_inicial_y] == " ",
                     True, False)):
        raise PositionOccupiedError
    elif orientacion == "sur" and not all(
        np.where(tablero[coordenada_inicial_x: coordenada_inicial_x + barcos[barco], coordenada_inicial_y] == " ",
                 True, False)):
        raise PositionOccupiedError
    elif orientacion == "este" and not all(
        np.where(tablero[coordenada_inicial_x, coordenada_inicial_y : coordenada_inicial_y - barcos[barco]:-1] == " ",
                 True, False)):
        raise PositionOccupiedError
    elif orientacion == "oeste" and not all(
        np.where(tablero[coordenada_inicial_x, coordenada_inicial_y : coordenada_inicial_y + barcos[barco]] == " ",
                 True, False)):
        raise PositionOccupiedError
    elif orientacion == "oeste" and coordenada_inicial_y - barcos[barco] > 10:
        raise OutOfBoundsError
    elif orientacion == "sur" and coordenada_inicial_x + barcos[barco] > 10:
        raise OutOfBoundsError
    elif orientacion == "norte" and coordenada_inicial_x + 1 - barcos[barco] < 0:
        print(coordenada_inicial_x - barcos[barco])
        raise OutOfBoundsError
    elif orientacion == "este" and coordenada_inicial_y  + 1 - barcos[barco] < 0:
        raise OutOfBoundsError
    elif orientacion == "sur":
        tablero[coordenada_inicial_x: coordenada_inicial_x + barcos[barco], coordenada_inicial_y] = "O"
    elif orientacion == "norte":
        tablero[coordenada_inicial_x - barcos[barco] + 1: coordenada_inicial_x + 1, coordenada_inicial_y] = "O"
    elif orientacion == "oeste":
        tablero[coordenada_inicial_x, coordenada_inicial_y - barcos[barco]: coordenada_inicial_y + barcos[barco]] = "O"
    elif orientacion == "este":
        tablero[coordenada_inicial_x, coordenada_inicial_y - barcos[barco] + 1: coordenada_inicial_y + 1] = "O"
    return tablero

def disparar(tablero, coordenada_x, coordenada_y):
    if tablero[coordenada_x, coordenada_y] == "O":
        tablero[coordenada_x, coordenada_y] = "X"
        print("Impacto")
    elif tablero[coordenada_x, coordenada_y] in ["X", "-"]:
        print("Ahí ya has disparado")
        nueva_coordenada_x = np.random.randint(low=0, high=10)
        nueva_coordenada_y = np.random.randint(low=0, high=10)
        disparar(tablero, nueva_coordenada_x, nueva_coordenada_y)
    else:
        tablero[coordenada_x, coordenada_y] = "-"
        print("Has fallado")
    return tablero


def contador_de_barcos(barcos_colocados, barco_a_colocar):
    if barco_a_colocar== "submarino" and barcos_colocados.count("submarino") > 3:
        return True
    elif barco_a_colocar == "fragata" and barcos_colocados.count("fragata") > 2:
        return True
    elif barco_a_colocar == "acorazado" and barcos_colocados.count("acorazado") > 1:
        return True
    elif barco_a_colocar == "portaaviones" and barcos_colocados.count("portaaviones") > 0:
        return True
    else:
        return False


fase_preliminar = True
inicio_juego = True
lista_de_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
barcos_colocados = []


while fase_preliminar:
    if inicio_juego is True:
        print(tablero_usuario)
        inicio_juego = False
    barco_a_colocar = input("Que barco quieres colocar?")
    while barco_a_colocar not in barcos.keys() or contador_de_barcos(barcos_colocados, barco_a_colocar):
        if barco_a_colocar not in barcos.keys():
            print("Ese barco no existe, solo puedes colocar portaaviones, acorazados, fragatas o submarinos")
        else:
            print("Ya has alcanzado el limite de esos barcos que puedes colocar")
        barco_a_colocar = input("Que barco quieres colocar?")
    else:
        coordenadas = input(
            f"Ese barco ocupa {barcos[barco_a_colocar]} espacios, introduce las coordenadas donde lo quieres colocar: ")
        while len(coordenadas.strip())>2:
            # FIX: Won't work if input is 10 (len = 3) and will break if user inputs some 2 char string like "pa"
            # USE REGEX TO SEE IF INPUT IS OF DESIRED FORMAT
            print("Esas coordenadas no son validas")
            coordenadas = input("Por favor introduce coordenadas validas")
        while coordenadas.upper().replace(" ", "")[0] not in lista_de_letras or not 0<int(coordenadas.replace(" ", "")[1])<11:
            print("Esa coordenada no existe")
            coordenadas = input("Por favor introduce coordenadas validas")
        coordenada_y = lista_de_letras.index(coordenadas.upper().replace(" ", "")[0])
        coordenada_x = int(coordenadas.replace(" ", "")[1]) - 1
        usuario_es_gilipollas = False

        usuario_coloca_barco = True
        if barco_a_colocar == "submarino":
            while usuario_coloca_barco:
                try:
                    tablero_usuario = colocar_submarino(tablero_usuario, coordenada_x, coordenada_y)
                    usuario_coloca_barco = False
                except PositionOccupiedError:
                    print("Esa posicion ya esta ocupada")
                    coordenadas = input(
                        "Introduce las coordenadas donde lo quieres colocar: ")
                    while coordenadas.upper().replace(" ", "")[0] not in lista_de_letras or not 0 < int(
                            coordenadas.replace(" ", "")[1]) < 10:
                        print("Esa coordenada no existe")
                        coordenadas = input("Por favor introduce coordenadas validas")
                    coordenada_y = lista_de_letras.index(coordenadas.upper().replace(" ", "")[0])
                    coordenada_x = int(coordenadas.replace(" ", "")[1]) - 1
        else:
            orientacion = input("En que orientacion quieres que este el barco? (norte, sur, este, oeste) ")
            orientacion = orientacion.lower()
            while orientacion not in ["norte", "sur", "este", "oeste"]:
                print("Orientacion no valida")
                orientacion = input("En que orientacion quieres que este el barco? (norte, sur, este, oeste)")
                orientacion = orientacion.lower()
            while usuario_coloca_barco:
                try:
                    tablero_usuario = colocar_barco(tablero_usuario, coordenada_x, coordenada_y, orientacion, barco_a_colocar)
                    usuario_coloca_barco = False
                except PositionOccupiedError:
                    print("Esa posicion ya esta ocupada")
                    coordenadas = input(f"Introduce las coordenadas donde lo quieres colocar: ")
                    orientacion = input("En que orientacion quieres que este el barco? (norte, sur, este, oeste)")
                    orientacion = orientacion.lower()
                    while orientacion not in ["norte", "sur", "este", "oeste"]:
                        print("Orientacion no valida")
                        orientacion = input("En que orientacion quieres que este el barco? (norte, sur, este, oeste)")
                        orientacion = orientacion.lower()
                    coordenada_y = lista_de_letras.index(coordenadas.upper().replace(" ", "")[0])
                    coordenada_x = int(coordenadas.replace(" ", "")[1]) - 1
                except OutOfBoundsError:
                    pass
    barcos_colocados.append(barco_a_colocar)
    print(tablero_usuario)
    if barcos_colocados.count("portaaviones") == 1 and barcos_colocados.count("acorazado") == 2 and\
            barcos_colocados.count("fragata") == 3 and barcos_colocados.count("submarino") == 4:
        fase_preliminar = False
# TODO: prettify printed tablero
# TODO: add loops for actual playability
# FIX: submarines cannot be placed facing outwards in the edges
#

