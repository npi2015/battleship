import numpy as np
from errors import *
import re


tablero_usuario = np.full((10,10), " ")
tablero_maquina = np.full((10,10), " ")
tablero_maquina_golpes = np.full((10,10), " ")
tablero_usuario_golpes = np.full((10,10), " ")
barcos = {"portaaviones" : 4, "acorazado" : 3, "fragata" : 2, "submarino" : 1}
lista_de_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def colocar_submarino(tablero, coordenada_inicial_x, coordenada_inicial_y):
    if tablero[coordenada_inicial_x, coordenada_inicial_y] != " ":
        raise PositionOccupiedError
    else:
        tablero[coordenada_inicial_x, coordenada_inicial_y] = "1"
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
    elif orientacion == "oeste" and coordenada_inicial_y + barcos[barco] > 10:
        raise OutOfBoundsError
    elif orientacion == "sur" and coordenada_inicial_x + barcos[barco] > 10:
        raise OutOfBoundsError
    elif orientacion == "norte" and coordenada_inicial_x + 1 - barcos[barco] < 0:
        raise OutOfBoundsError
    elif orientacion == "este" and coordenada_inicial_y  + 1 - barcos[barco] < 0:
        raise OutOfBoundsError
    elif orientacion == "sur":
        tablero[coordenada_inicial_x: coordenada_inicial_x + barcos[barco], coordenada_inicial_y] = barcos[barco]
    elif orientacion == "norte":
        tablero[coordenada_inicial_x - barcos[barco] + 1: coordenada_inicial_x + 1, coordenada_inicial_y] = barcos[barco]
    elif orientacion == "oeste":
        tablero[coordenada_inicial_x, coordenada_inicial_y: coordenada_inicial_y + barcos[barco]] = barcos[barco]
    elif orientacion == "este":
        tablero[coordenada_inicial_x, coordenada_inicial_y - barcos[barco] + 1: coordenada_inicial_y + 1] = barcos[barco]
    return tablero

def disparar(tablero, coordenada_x, coordenada_y):
    if tablero[coordenada_x, coordenada_y] in ["1", "2", "3", "4"]:
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

def valid_input(coordenadas):
    x = re.match("^[a-jA-J][1-9]$", coordenadas.strip())
    y = re.match("^[a-jA-J]10$", coordenadas.strip())
    while x is None and y is None:
        print("Esas coordenadas no son validas")
        print(coordenadas)
        coordenadas = input("Por favor introduce coordenadas validas")
        x = re.match("^[a-jA-J][1-9]$", coordenadas.strip())
        y = re.match("^[a-jA-J]10$", coordenadas.strip())
    columna = lista_de_letras.index(coordenadas.strip()[0])
    if x:
        fila = int(coordenadas.strip()[1]) - 1
    if y:
        fila = 9
    return columna, fila

def orientacion_valida():
    orientacion = input("En que orientacion quieres que este el barco? (norte, sur, este, oeste) ")
    orientacion = orientacion.lower()
    while orientacion not in ["norte", "sur", "este", "oeste"]:
        orientacion = input("Orientacion no valida (norte, sur, este, oeste)")
        orientacion = orientacion.lower()
    return orientacion

juego_en_progreso = False


def crear_tablero(tablero, usuario = False, maquina = False):
    fase_preliminar = True
    if maquina:
        barcos_colocados_maquina = []
        while fase_preliminar:
            barco_a_colocar = np.random.choice(list(barcos.keys()))
            while contador_de_barcos(barcos_colocados_maquina, barco_a_colocar):
                barco_a_colocar = np.random.choice(list(barcos.keys()))
            else:
                coordenadas = "".join(map(str,np.array(np.meshgrid(lista_de_letras, np.arange(1,11))).T.reshape(-1,2)[np.random.randint(0,100)]))
                coordenada_y, coordenada_x = valid_input(coordenadas)
                maquina_coloca_barco = True
                if barco_a_colocar == "submarino":
                    while maquina_coloca_barco:
                        try:
                            tablero = colocar_submarino(tablero, coordenada_x, coordenada_y)
                            maquina_coloca_barco = False
                        except PositionOccupiedError:
                            coordenadas = "".join(
                                map(str, np.array(np.meshgrid(lista_de_letras, np.arange(1,11))).T.reshape(-1, 2)[np.random.randint(0, 100)]))
                            coordenada_x, coordenada_y = valid_input(coordenadas)
                else:
                    orientacion = np.random.choice(["norte", "sur", "este","oeste"])
                    while maquina_coloca_barco:
                        try:
                            tablero = colocar_barco(tablero, coordenada_x, coordenada_y, orientacion, barco_a_colocar)
                            maquina_coloca_barco = False
                        except PositionOccupiedError:
                            coordenadas = "".join(map(str,np.array(np.meshgrid(lista_de_letras, np.arange(1,11))).T.reshape(-1,2)[np.random.randint(0,100)]))
                            coordenada_x, coordenada_y = valid_input(coordenadas)
                            orientacion = np.random.choice(["norte", "sur", "este", "oeste"])
                        except OutOfBoundsError:
                            coordenadas = "".join(
                                map(str, np.array(np.meshgrid(lista_de_letras, np.arange(1,11))).T.reshape(-1, 2)[np.random.randint(0, 100)]))
                            coordenada_x, coordenada_y = valid_input(coordenadas)
                            orientacion = np.random.choice(["norte", "sur", "este", "oeste"])
            barcos_colocados_maquina.append(barco_a_colocar)
            if barcos_colocados_maquina.count("portaaviones") == 1 and barcos_colocados_maquina.count("acorazado") == 2 and\
                    barcos_colocados_maquina.count("fragata") == 3 and barcos_colocados_maquina.count("submarino") == 4:
                fase_preliminar = False
                return tablero
    elif usuario:
        barcos_colocados = []
        inicio_juego = True
        while fase_preliminar:
            if inicio_juego is True:
                print(tablero)
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
                coordenada_y, coordenada_x = valid_input(coordenadas)
                usuario_coloca_barco = True
                if barco_a_colocar == "submarino":
                    while usuario_coloca_barco:
                        try:
                            tablero = colocar_submarino(tablero, coordenada_x, coordenada_y)
                            usuario_coloca_barco = False
                        except PositionOccupiedError:
                            print("Esa posicion ya esta ocupada")
                            coordenadas = input(
                                "Introduce las coordenadas donde lo quieres colocar: ")
                            coordenada_x, coordenada_y = valid_input(coordenadas)
                else:
                    orientacion = orientacion_valida()
                    while usuario_coloca_barco:
                        try:
                            tablero = colocar_barco(tablero, coordenada_x, coordenada_y, orientacion,
                                                            barco_a_colocar)
                            print("Barco colocado")
                            usuario_coloca_barco = False
                        except PositionOccupiedError:
                            print("Esa posicion ya esta ocupada")
                            coordenadas = input("Introduce las coordenadas donde lo quieres colocar: ")
                            coordenada_x, coordenada_y = valid_input(coordenadas)
                            orientacion = orientacion_valida()
                        except OutOfBoundsError:
                            print("El barco se sale del tablero")
                            coordenadas = input("Introduce las coordenadas donde lo quieres colocar: ")
                            coordenada_x, coordenada_y = valid_input(coordenadas)
                            orientacion = orientacion_valida()
            barcos_colocados.append(barco_a_colocar)
            print(tablero)
            if barcos_colocados.count("portaaviones") == 1 and barcos_colocados.count("acorazado") == 2 and \
                    barcos_colocados.count("fragata") == 3 and barcos_colocados.count("submarino") == 4:
                fase_preliminar = False
                return  tablero
    else:
        return None

# TODO: prettify printed tablero
# TODO: add loops for actual playability
# FIX: submarines cannot be placed facing outwards in the edges

