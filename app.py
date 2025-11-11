#Importaciones
from ttt_core import *
#Definiciones
def jugar():
    opcion = input("Bienvenido al tres en raya\n1. Jugador vs Jugador\n2. Jugador vs CPU\nElige una opción: ")
    tablero = crear_tablero()
    jugador = 1
    terminado = False
    while terminado == False:
        mostrar_tablero(tablero)
        fila = -1
        columna = -1
        movimiento_hecho = False
        if opcion == "2" and jugador == 2:
            print("Turno de la CPU")
            (fila, columna) = movimiento_cpu(tablero)
            print("CPU juega en:", fila, columna)
            movimiento_hecho = True
        else:
            while movimiento_hecho == False:
                try:
                    fila = int(input("Fila (0-2): "))
                    columna = int(input("Columna (0-2): "))
                except:
                    print("Eso no es un número válido")
                    fila = -1
                    columna = -1
                valido = movimiento_valido(tablero, fila, columna)
                if valido == True:
                    movimiento_hecho = True
                else:
                    print("Movimiento no válido, inténtalo otra vez")
#Colocar la ficha si se puede
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = jugador
        if hay_victoria(tablero, jugador):
            mostrar_tablero(tablero)
            if jugador == 1:
                print("Gana el jugador X")
            else:
                print("Gana el jugador O")
            terminado = True
        else:

            if tablero_lleno(tablero):
                mostrar_tablero(tablero)
                print("Empate, nadie gana ")
                terminado = True
            else:
                if jugador == 1:
                    jugador = 2
                else:
                    jugador = 1
    print("Fin del juego")

jugar()
