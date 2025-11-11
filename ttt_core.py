import numpy as np
import random

def crear_tablero():
    tablero = np.zeros((3, 3), dtype=int)
    return tablero

def mostrar_tablero(tablero):
    simbolos = {0: "[]", 1: "X", 2: "O"}
    for f in range(3):
        linea = ""
        for c in range(3):
            linea = linea + simbolos[tablero[f][c]] + "  "
        print(linea)
        print(" " * 9)

def hay_victoria(tablero, jugador):
    for i in range(3):
        if np.all(tablero[i, :] == jugador):
            return True
        if np.all(tablero[:, i] == jugador):
            return True
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False

def tablero_lleno(tablero):
    lleno = True
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 0:
                lleno = False
    return lleno

def movimiento_valido(tablero, fila, columna):
    if fila < 0 or fila > 2:
        return False
    if columna < 0 or columna > 2:
        return False
    if tablero[fila][columna] != 0:
        return False
    return True

def movimiento_cpu(tablero):
    vacias = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 0:
                vacias.append((i, j))
    eleccion = random.choice(vacias)
    return eleccion
