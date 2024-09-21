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
#incumbente_inicial:np.ndarray =   # se almacena el incumbente inicial para comparar con el de la mejor solución
#fo_inicial:int =   # se almacena el valor de la función objetivo del incumbente para comparar con el de la mejor solución

#generación de vecindario aleatorias a través de permutaciones
#vecindario:np.ndarray =    # inicializa array
#Tamano_vecindario:int = 

# generación de vecindario
### inserte aquí su código ###

#print(vecindario)

#iniciar historia tabu
#memoria_tabu:np.ndarray =    # inicializa variable

### inicio exploración de vecindarios a través de un vecino ###
iter:int = 0

#with tqdm(total=len(range(Tamano_vecindario))) as pbar:
    #while iter < Tamano_vecindario:
        
        #seleccionar un vecino aleatorio del vecindario
        #indice_vecino_aleatorio:int = 
        #vecino = 

        #generar candidatos a mejoramiento a partir de un vecino usando operadores de intercambio
        #vecindario_candidatos:np.ndarray =     #inicializa variable
        #movimientos_candidatos:np.ndarray =    #inicializa variable
        
        #for i in range(Tamano_vecindario_explorar):
        
            #nuevo_vecino, movimiento = opt_operator(vecino,memoria_tabu)
            #vecindario_candidatos[i,:] = 
            
            #insertar la tupla de movimientos en el vector de movimientos candidatos
            #movimientos_candidatos[i,:] = 

        #iniciar vector de funciones objetivo
        #fo_v:np.ndarray = np.zeros(Tamano_vecindario_explorar,dtype=int) # funciones objetivo del vencidario. Inicializar variable
        
        #obtener funciones objetivo de cada vecindario
        ### inserte aquí su código ###
        #print(fo_v)

        #inicializar valor de la función objetivo actual en infinito
        #fo_iter:int = 100000

        #inicio verificación del vecindario respecto a la incumbente
        #indice_vecino_mejora: int = -1 # variable que almacena indice
        ### inserte aquí su código (verificación vecino con incumbente) ###
        
        
        # actualizar incumbente y memoría tabu memoria tabú
        #if XXXX < XXXX:
            #fo_incumbente = 
            #incumbente = 
            #memoria_tabu[X,Y] = 
            #memoria_tabu[Y,X] = 
        #else:
            # definir la variable <condicion> de tipo bool que verifique si memoria_tabu es mayor que cero
            #condicion = 
            # actualizar memoría tabu de acuerdo al valor en <condicion>
            #memoria_tabu = 
        
        # actualizar contador de iteraciones
         ### inserte aquí su código ###
        
        #pbar.set_description(f"fo_incumbente: {fo_incumbente}")
        #pbar.update()

    #pbar.close()

#print(f"La función objetivo inicial era: {fo_inicial}")
#print(f"La solución inicial era: {incumbente_inicial}")
#print(f"La función objetivo despues de usar TS es: {fo_incumbente}")
#print(f"La solución despues de usar TS es: {incumbente}")

