# @autor : Alejandro Lainez gonzalez
#@fecha : 2023/10/19
#@descripcion : programa principal para el juego
#          de busca mina 

# modulos propios de python
#math.ceil(x) redondea el numero jacia arriba al entorno mas cercano.
import math
import random
import os


#crear el valor de la mina
MINA = -1

# Funciones de back-end para el juego buscaminas
# Funcion para crear
# 
# el tablero de buscaminas 

def crear_tablero(nro_fila, nro_clos, porc_minas =  30):
    # crear por comprension la lista el tablero de 
    # buscaminas
    tablero = [[0 for j in range (nro_clos)]for i in range(nro_fila)]
    
    insertar_minas(tablero, porc_minas)
    conteo_minas(tablero)
    conteo_minas_izquierda(tablero)
    conteo_minas_derecha(tablero)
    conteo_minas_superior(tablero)
    # conteo_minas_inferior(tablero)
    # conteo_de_minas_esquina_superior(tablero)
    conteo_de_minas_esquina_superior_derecha(tablero)
    conteo_de_minas_esquina_superior_izquierda(tablero)
    conteo_de_minas_esquina_inferior_izquierda(tablero)
    conteo_de_minas_esquina_inferior_derecha(tablero)
    return tablero

#funcion para insertar las minas en el tablero
def insertar_minas(tablero, porc_minas):
    #definir el contado de minas
    
    cont_minas = 0
    #calcular el numero de minas a insertar en el tablero
    filas = len(tablero)
    columnas = len(tablero[0])
    # math.ceil(x) redondea el numero jacia arriba al entorno mas cercano.
    nro_minas = math.ceil (filas * columnas * (porc_minas/100))
    
    while cont_minas < nro_minas: 
        #elegir una fila y una columna al alzar
        fila = random.randrange(0, filas )
        columna = random.randrange(0, columnas )
        
        # preguntamos si la celda elegida aun no contiene minas
        if tablero[fila] [columna] != MINA:
            tablero[fila] [columna] = MINA
            cont_minas += 1
        else:
            continue  
        
        #funcion para el conteo de minas alrededor de cada una 
        # de las celdas
        
def conteo_minas(tablero):
    #realizar el recorrido sobre el tablero por indices
    
    filas = len(tablero)
    columnas = len(tablero[0])
    
    for i in range(1, filas - 1):
        for j in range(1, columnas - 1): 
            if tablero[i][j] != MINA:
                if tablero[i - 1] [j - 1] == MINA:
                    tablero[i][j] += 1
                    
                if tablero[i - 1] [j] == MINA:
                    tablero[i][j] += 1
                    
                if tablero[i - 1] [j + 1] == MINA:
                    tablero[i][j] += 1
                    
                if tablero[i] [j - 1] == MINA:
                    tablero[i][j] += 1
                    
                if tablero[i] [j + 1] == MINA:
                    tablero[i][j] += 1
                    
                if tablero[i + 1] [j - 1] == MINA:
                    tablero[i][j] += 1
                    
                if tablero[i + 1] [j] == MINA:
                    tablero[i][j] += 1
                    
                if tablero[i + 1] [j + 1] == MINA:
                    tablero[i][j] += 1

# funcion para hallar las minas en le extremo izquierdo sin tener encuenta 
# la esquina superior izquierda 
# y la esquina interior izquierda 
def conteo_minas_izquierda(tablero):
    filas = len(tablero)
    for i in range(1,filas-1):
        if tablero[i][0] != MINA:
            if tablero[i-1][0] == MINA:
                tablero[i][0] += 1
            if tablero[i-1][1] == MINA:
                tablero[i][0] += 1
            if tablero[i][1] == MINA:
                tablero[i][0] += 1
            if tablero[i+1][0] == MINA:
                tablero[i][0] += 1
            if tablero[i+1][1] == MINA:
                tablero[i][0] += 1
                
# funcion para hallar las minas en le extremo derecho sin tener encuenta 
# la esquina superior izquierda 
# y la esquina interior izquierda            
def conteo_minas_derecha(tablero):
    filas = len(tablero)
    
    for i in range(1, filas - 1):
        if tablero[i] [-1] != MINA:
            
            if tablero[i - 1][-1] == MINA:
                tablero [i][-1] += 1
                
            if tablero[i - 1][-2] == MINA:
                tablero [i][-1] += 1
                
            if tablero[i][-2] == MINA:
                tablero [i][-1] += 1
                
            if tablero[i + 1 ][-1] == MINA:
                tablero [i][-1] += 1
                
            if tablero[i + 1 ][-2] == MINA:
                tablero [i][-1] += 1
                
# #Funcion para hallar las minas en el extremo superior               
def conteo_minas_superior(tablero):
    columna = len(tablero)
    
    for j in range(1, columna - 1):
        if tablero[0] [j] != MINA:
            
            if tablero[0][j - 1] == MINA:
                tablero[0][j] += 1
                
            if tablero[0][j + 1] == MINA:
                tablero [0][j] += 1
                
            if tablero[1][j - 1] == MINA:
                tablero[0][j] += 1
                
            if tablero[1 ][j] == MINA:
                tablero [0][j] += 1
                
            if tablero[1][j + 1] == MINA:
                tablero [0][j] += 1


#funcion para hallar las minas en el extremo inferior del tablero

def conteo_minas_inferior(tablero):
    columna = len(tablero[0])
    
    for j in range(1, columna - 1):
        if tablero[-1] [j] != MINA:
            
            if tablero[-1][j - 1] == MINA:
                tablero[-1][j] += 1
                
            if tablero[-1][j + 1] == MINA:
                tablero [-1][j] += 1
                
            if tablero[-2][j - 1] == MINA:
                tablero[-1][j] += 1
                
            if tablero[-2][j] == MINA:
                tablero [-1][j] += 1
                
            if tablero[-2][j + 1] == MINA:
                tablero [-1][j] += 1
                

# funcion para el conteo de minas al rededor de cada una de las 
# celdas
def conteo_de_minas_esquina_superior(tablero):
    
    columnas = len(tablero)
    for j in range(1,columnas-1):
        if tablero[0][j] != MINA:
            if tablero[1][j] == MINA:
                tablero[0][j] += 1
            if tablero[1][j-1] == MINA:
                tablero[0][j] += 1
            if tablero[0][j-1] == MINA:
                tablero[0][j] += 1

#### funcion para contar las minas en la esquina superior derecha
def conteo_de_minas_esquina_superior_derecha(tablero):
    
    columnas = len(tablero)
    if tablero[0][columnas-1] != MINA:
        if tablero[1][columnas-1] == MINA:
            tablero[0][columnas-1] += 1
        if tablero[1][columnas-2] == MINA:
            tablero[0][columnas-1] += 1
        if tablero[0][columnas-2] == MINA:
            tablero[0][columnas-1] += 1

## funcion para contar las minas en la esquina superior izquierda
def conteo_de_minas_esquina_superior_izquierda(tablero):
    
    
    if tablero[0][0] != MINA:
        if tablero[1][0] == MINA:
            tablero[0][0] += 1
        if tablero[1][1] == MINA:
            tablero[0][0] += 1
        if tablero[0][1] == MINA:
            tablero[0][1] += 1

## funcion para contar las minas en la esquina inferior izquierda
def conteo_de_minas_esquina_inferior_izquierda(tablero):
    if tablero[-1][0] != MINA:
        if tablero[-2][0] == MINA:
            tablero[-1][0] +=1
        if tablero[-2][1] == MINA:
            tablero[-1][0] +=1
        if tablero[-1][1] == MINA:
            tablero[-1][0] +=1


##funcion para contar las minas en la esquina inferior derecha
def conteo_de_minas_esquina_inferior_derecha(tablero):
    if tablero[-1][-1] != MINA:
        if tablero[-2][-1] == MINA:
            tablero[-1][-1] +=1
        if tablero[-2][-2] == MINA:
            tablero[-1][-1] +=1
        if tablero[-1][-2] == MINA:
            tablero[-1][-1] +=1