import numpy as np
from funcionObjetivo import funcionObjetivo
from opt_operator import opt_operator
from tqdm import tqdm
import random

######## Algoritmo de búsqueda tabu para el problema de asignación ########

#establecer semilla (0) de numeros aleatorios en numpy
np.random.seed(0)
random.seed(0)

#generar matriz de costos para problema de asignación
numero_agentes:int = 50
numero_tareas:int = 50

# Parametros
numero_vecinos:int = 8000
Tamano_vecindario_explorar:int = 10
periodo_tabu:int = 10

# definir matriz de costos aleatoría
costos:np.ndarray = np.random.randint(1,10,size=(numero_agentes,numero_tareas),dtype=int)
#print(costos) # Se deja como comentario, porque ya verificamos que se este generando la matriz de costo segun lo esperado

# construcción de solución e incumbente inicial
incumbente:np.ndarray =  np.random.permutation(numero_agentes) # Por defecto, la permutacion toma valores enteros
fo_incumbente:int = funcionObjetivo(incumbente,costos)
incumbente_inicial:np.ndarray =  incumbente.copy() # se almacena el incumbente inicial para comparar con el de la mejor solución
fo_inicial:int = fo_incumbente  # se almacena el valor de la función objetivo del incumbente para comparar con el de la mejor solución

#generación de vecindario aleatorias a través de permutaciones
vecindario:np.ndarray = np.zeros((numero_vecinos,numero_tareas), dtype=int)   # inicializa array
Tamano_vecindario:int = numero_vecinos

# generación de vecindario
for agente in range(numero_vecinos):
    vecino = np.random.permutation(numero_agentes)
    vecindario[agente,:] = vecino

#print(vecindario)

#iniciar historia tabu
memoria_tabu:np.ndarray = np.zeros((numero_agentes,numero_tareas), dtype=int)   # inicializa variable

### inicio exploración de vecindarios a través de un vecino ###
iter:int = 0

with tqdm(total=len(range(Tamano_vecindario))) as pbar:
    while iter < Tamano_vecindario:
        
        #seleccionar un vecino aleatorio del vecindario
        indice_vecino_aleatorio:int = np.random.randint(Tamano_vecindario)
        vecino = vecindario[indice_vecino_aleatorio,:]

        #generar candidatos a mejoramiento a partir de un vecino usando operadores de intercambio
        vecindario_candidatos:np.ndarray = np.zeros((Tamano_vecindario_explorar,numero_tareas), dtype=int)   #inicializa variable
        movimientos_candidatos:np.ndarray = np.zeros((Tamano_vecindario_explorar,2), dtype=int)  #inicializa variable
        
        for i in range(Tamano_vecindario_explorar):
            
            nuevo_vecino, movimiento = opt_operator(vecino,memoria_tabu)
            vecindario_candidatos[i,:] = nuevo_vecino
            
            #insertar la tupla de movimientos en el vector de movimientos candidatos
            movimientos_candidatos[i,:] = movimiento

        #iniciar vector de funciones objetivo
        fo_v:np.ndarray = np.zeros(Tamano_vecindario_explorar,dtype=int) # funciones objetivo del vencidario. Inicializar variable
        
        #obtener funciones objetivo de cada vecindario
        for i in range(Tamano_vecindario_explorar):
            fo_v[i] = funcionObjetivo(vecindario_candidatos[i,:],costos)
        #print(fo_v)

        #inicializar valor de la función objetivo actual en infinito
        fo_iter:int = 100000

        #inicio verificación del vecindario respecto a la incumbente
        indice_vecino_mejora: int = -1 # variable que almacena indice
        for i in range(Tamano_vecindario_explorar):
            if fo_v[i] < fo_iter:
                fo_iter = fo_v[i]
                indice_vecino_mejora = i
        
        # actualizar incumbente y memoría tabu memoria tabú
        if fo_iter < fo_incumbente:
            fo_incumbente = fo_iter
            incumbente = vecindario_candidatos[indice_vecino_mejora,:]
            memoria_tabu[movimientos_candidatos[indice_vecino_mejora,0],movimientos_candidatos[indice_vecino_mejora,1]] = periodo_tabu
            memoria_tabu[movimientos_candidatos[indice_vecino_mejora,1],movimientos_candidatos[indice_vecino_mejora,0]] = periodo_tabu
        else:
            # definir la variable <condicion> de tipo bool que verifique si memoria_tabu es mayor que cero
            condicion = memoria_tabu > 0
            # actualizar memoría tabu de acuerdo al valor en <condicion>
            memoria_tabu = np.where(condicion,memoria_tabu-1,memoria_tabu)
        
        # actualizar contador de iteraciones
        iter += 1
        
        pbar.set_description(f"fo_incumbente: {fo_incumbente}")
        pbar.update()

    pbar.close()

print(f"La función objetivo inicial era: {fo_inicial}")
print(f"La solución inicial era: {incumbente_inicial}")
print(f"La función objetivo despues de usar TS es: {fo_incumbente}")
print(f"La solución despues de usar TS es: {incumbente}")

