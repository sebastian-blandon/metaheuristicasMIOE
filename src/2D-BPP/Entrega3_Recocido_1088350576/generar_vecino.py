import numpy as np
import random


def generar_vecino_inicial(dims, semilla):

    np.random.seed(semilla)
    random.seed(semilla)

    # Establecer solucion inicial como una permutacion
    numero_objetos = dims.shape[0]
    solucion_inicial = np.random.permutation(numero_objetos)

    # Generar matriz de solución que en la columnas 1 este la solución inicial y las columnas 2 y 3 esten las dimensiones correspondientes
    # inicializar como matriz de dimensiones (dim,3)
    matriz_solucion = np.zeros((numero_objetos, 3), dtype=int)

    # incluir solución inicial en la matriz de soluciones
    matriz_solucion[:, 0] = solucion_inicial
    # extraer las dimensiones de la solución inicial 
    matriz_solucion[:, 1:] = dims[solucion_inicial]
    # solucion como las dimensiones de la secuencia de elementos (columnas 2 y 3)
    solucion = matriz_solucion[:, 1:]
    
    return solucion,matriz_solucion


def generar_vecino(solucion):

    #np.random.seed(semilla)
    #random.seed(semilla)

    # Indices of the elements to swap randomly
    index1, index2 = np.random.choice(len(solucion), 2, replace=False)
    
    # Save the value of solucion[index1]
    temp = solucion[index1].copy()
    
    # Assign the value of solucion[index2] to solucion[index1]
    solucion[index1] = solucion[index2]
    
    # Assign the saved value to solucion[index2]
    solucion[index2] = temp
    
    return solucion