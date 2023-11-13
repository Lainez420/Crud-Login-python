# @autor : Alejandro Lainez Gonzalez
#@fecha : 2023/10/19
#@descripcion : programa principal para el juego
#          de busca mina  
 
# # llamada de modulos propios para el  buscaminas
from modulobm import bsuca_mina as bm

print("Bienvenido al juego de busca minas por consola")
filas = int(input("ingrese el numero de filas del tablero"))
columnas = int(input("ingrese el numero de columnas del tablero"))
#crear tablero de busca mina
tablerobm = bm.crear_tablero(filas, columnas)

#recorrido del tablero por indices 
for i in range(filas) :
    print("[", end = " ")
    for j in range(columnas) :
        print(f"{tablerobm[i][j]:2d}", end = ", " )
    print(" ]")

