import numpy as np

def mutacion(mejor_hijo,tasa_mutacion,numero_objetos):
    
    # realizar copia de mejor hijo para no modificar el original
    mejor_hijo_mutado = mejor_hijo.copy()
    
    # definir número de mutaciones a realizar
    num_mutaciones = int(tasa_mutacion * numero_objetos)
    
    # lanzar aleatorio y verificar si se requiere mutar
    if np.random.rand() < tasa_mutacion: # Verifico si debe mutar
        for i in range(num_mutaciones):
            # mutación como un cambio de un valor binario en un indice aleatorio
            indice_aleatorio = np.random.randint(0, numero_objetos)
            mejor_hijo_mutado[indice_aleatorio] = np.random.randint(0, 2) # para generar aleatorios binarios

    return mejor_hijo_mutado