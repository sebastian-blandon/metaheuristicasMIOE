import numpy as np
import random
import plotly.express as px
from tqdm import tqdm

from poblacion_inicial import poblacion_inicial
from seleccionPadres import seleccionPadres
from cruzamiento import cruzamiento
from funcion_objetivo import funcion_objetivo,funcion_objetivo_pop
from mutacion import mutacion
from distancias import distancias # Tomando la funcion creada para el TSP con colonia de hormigas

# configuración semilla numeros aleatorios
np.random.seed(0)
random.seed(0)

# instancia el problema: obtener coordenadas de las ciudades y la distancia entre ellas
tamanio_poblacion = 10 # Circuitos
numero_ciudades = 26
coordenadas_ciudades = np.random.rand(numero_ciudades, 2)
matriz_distancias = distancias(coordenadas_ciudades)

print(f"Coordenadas de las ciudades: , {coordenadas_ciudades}")
#print(f"Distancias: , {matriz_distancias}") # La dejo comentada porque la matriz es grande y uno agrega mucho valor el mostrar dichas distancias


# parámetros genético: obtener tamaño_poblacion, k (individuos candidatos a padres), tasa_mutacion
maximo_iteraciones = numero_ciudades*1000
k = 3 # Ciudades candidatas a ser padres
tasa_mutacion = 0.7

# construir poblacion inicial: obtener poblacion, peso_poblacion, funciones_objetivo_pop
print("\n Generando poblacion inicial...\n")
poblacion = poblacion_inicial(tamanio_poblacion,numero_ciudades)
print(poblacion)


# obtener incumbente desde población: obtener incumbente, solucion_incumbente, peso_incumbente, historia_incumbente
print("\n Obteniendo incumbente inicial...\n")
#funcion_objetivo_pop = np.sum(poblacion*precio_objetos,axis=1) # Del ejercicio de la mochila
funcion_objetivo_pop = funcion_objetivo_pop(poblacion,matriz_distancias)
print(f"funcion_objetivo_pop: {funcion_objetivo_pop}")
print("")

incumbente = np.min(funcion_objetivo_pop) # La incumbente es la mejor de todas las soluciones
incumbente_inicial = incumbente.copy()
indice_incumbente = np.argmin(funcion_objetivo_pop)
solucion_incumbente = poblacion[indice_incumbente]


historia_incumbente = [] # Se usan con las que salen de la evolución
# Ingreso mi primera incumbente a la historia
historia_incumbente.append(incumbente)

print(f"Incumbente_inicial: {incumbente}")
print(f"Indice incumbente: {indice_incumbente}")
print(f"Solución incumbente_inicial: {solucion_incumbente}")
print("")

# inicio evolucion
with tqdm(total=len(range(maximo_iteraciones))) as pbar:
    for i in range(maximo_iteraciones):
        # seleccionar padres
        padres = seleccionPadres(k,funcion_objetivo_pop,poblacion,tamanio_poblacion) 

        # Cruzamiento
        hijos = cruzamiento(padres)
        
        # selección del mejor hijo
        func_obj = funcion_objetivo(hijos,matriz_distancias,incumbente_inicial) 

        # mejor hijo como el que tenga mejor función objetivo
        indice_mejor_hijo = np.argmax(func_obj)
        #print(indice_mejor_hijo)

        mejor_hijo = hijos[indice_mejor_hijo]

        # mutación
        mejor_hijo_mutado = mutacion(mejor_hijo,tasa_mutacion,numero_objetos)
        
        # extraer el valor de la función objetivo del objeto de retorno de "funcion_objetivo" 
        func_obj_mutado,peso_hijo_mutado = funcion_objetivo([mejor_hijo_mutado], precio_objetos,peso_objetos,peso_maximo_mochila)

        # mejor hijo mutado como el que tenga mejor función objetivo
        
        # Requiero ingresar mejor_hijo_mutado a la poblacion
        # verificar si solución existe en población
    
        indices_si_existe = np.where((poblacion == mejor_hijo_mutado).all(axis=1))  # verifica cada vector de la población con el mejor hijo mutado.

        


        ingresa = False # Ingresa a la poblacion
        if len(indices_si_existe[0]) == 0: # Verifica si existe
            peso_hijo_mutado = peso_hijo_mutado[0]
            # verificar si es factible por peso y si es mejor que incumbente para ingresar a población
            if peso_hijo_mutado < peso_maximo_mochila and func_obj_mutado > incumbente:
                ingresa = True

        # actualización de la población
        if ingresa:
            # encontrar miembro de la población con menor función objetivo
            posicion_menor = np.argmin(funcion_objetivo_pop)
            # actualizar miembro de la población con menor función objetivo con el mejor hijo mutado y su función objetivo
            poblacion[posicion_menor] = mejor_hijo_mutado
            funcion_objetivo_pop[posicion_menor] = func_obj_mutado[0]
            #print("")
            # actualizar incumbente
            incumbente = func_obj_mutado[0]
            solucion_incumbente = mejor_hijo_mutado
            # anexar incumbente a la historia_icumbente
            historia_incumbente.append(incumbente)
        
        pbar.set_description(f"fo_incumbente: {incumbente}") # activar para la barra de progreso
        pbar.update() # activar para la barra de progreso
    

#solucion_incumbente = 
#peso_incumbente = 
print(f"\n Solución incumbente: {solucion_incumbente} \n")
print(f"peso incumbente: {peso_incumbente} \n")

# gráfico de mejoramiento de función objetivo
fig = px.line(historia_incumbente)
fig.show()