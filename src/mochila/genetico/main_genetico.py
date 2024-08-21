import numpy as np
import random
import plotly.express as px
from tqdm import tqdm

from poblacion_inicial import poblacion_inicial
from seleccionPadres import seleccionPadres
from cruzamiento import cruzamiento
from funcion_objetivo import funcion_objetivo
from mutacion import mutacion

# configuración semilla numeros aleatorios
np.random.seed(0)
random.seed(0)

# instancia el problema: obtener peso_objetos, precio_objetos
tamanio_poblacion = 10
numero_objetos = 30
peso_maximo_mochila = 500
peso_maximo_objeto = 50
precio_maximo = 100
peso_objetos = np.random.randint(1, peso_maximo_objeto, numero_objetos)
precio_objetos = np.random.randint(1, precio_maximo, numero_objetos)

print(f"Precio objetos: , {precio_objetos}")
print(f"Peso objetos: , {peso_objetos}")

# parámetros genético: obtener tamaño_poblacion, k (individuos candidatos a padres), tasa_mutacion
maximo_iteraciones = numero_objetos*1000
k = 3 # Individuos candidatos a ser padres
tasa_mutacion = 0.7

# construir poblacion inicial: obtener poblacion, peso_poblacion, funciones_objetivo_pop
print("\n Generando poblacion inicial factible...\n")
poblacion = poblacion_inicial(tamanio_poblacion,numero_objetos,peso_maximo_mochila,peso_objetos)
print(poblacion)

# obtener incumbente desde población: obtener incumbente, solucion_incumbente, peso_incumbente, historia_incumbente
print("\n Obteniendo incumbente inicial...\n")
funcion_objetivo_pop = np.sum(poblacion*precio_objetos,axis=1)
print(f"funcion_objetivo_pop: {funcion_objetivo_pop}")


incumbente = np.max(funcion_objetivo_pop) # La incumbente es la mejor de todas las soluciones
indice_incumbente = np.argmax(funcion_objetivo_pop)
solucion_incumbente = poblacion[indice_incumbente]
peso_incumbente = np.sum(solucion_incumbente*peso_objetos)
historia_incumbente = [] # Se usan con las que salen de la evolución
# Ingreso mi primera incumbente a la historia
historia_incumbente.append(incumbente)

print(f"Incumbente_inicial: {incumbente}")
print(f"Indice incumbente: {indice_incumbente}")
print(f"Solución incumbente_inicial: {solucion_incumbente}")
print(f"Peso incumbente: {peso_incumbente}")


# inicio evolucion
with tqdm(total=len(range(maximo_iteraciones))) as pbar:
    for i in range(maximo_iteraciones):
        # seleccionar padres
        padres = seleccionPadres(k,funcion_objetivo_pop,poblacion,tamanio_poblacion,numero_objetos) 

        # Cruzamiento
        #hijos = cruzamiento(padres)

        # selección del mejor hijo
        #func_obj = funcion_objetivo(hijos,precio_objetos,peso_objetos,peso_maximo)
        
        # mejor hijo como el que tenga mejor función objetivo
        #mejor_hijo = 

        # mutación
        #mejor_hijo_mutado = mutacion(mejor_hijo,tasa_mutacion,numero_objetos)
        #func_obj_mutado,_ = funcion_objetivo([mejor_hijo_mutado], precio_objetos,peso_objetos,peso_maximo)
        
        # extraer el valor de la función objetivo del objeto de retorno de "funcion_objetivo" 
        #func_obj_mutado = 

        # verificar si solución existe en población
        #ingresa = False
        #indices = np.where((poblacion == mejor_hijo_mutado).all(axis=1))  # verifica cada vector de la población con el mejor hijo mutado.
        #if len(indices[0]) == 0:
            #peso_hijo_mutado = 
            # verificar si es factible por peso y si es mejor que incumbente para ingresar a población
            #if peso_hijo_mutado < peso_maximo and func_obj_mutado > incumbente:
            #    ingresa = True

        # actualización de la población
        #if ingresa:
            # encontrar miembro de la población con menor función objetivo
            #posicion_menor = 
            # actualizar miembro de la población con menor función objetivo con el mejor hijo mutado y su función objetivo
            #poblacion[posicion_menor] = 
            #funciones_objetivo_pop[posicion_menor] = 

        # actualizar incumbente
        #incumbente = 
        #solucion_incumbente = 
        # anexar incumbente a la historia_icumbente
        #historia_incumbente...
        
        #pbar.set_description(f"fo_incumbente: {incumbente}") # activar para la barra de progreso
        #pbar.update() # activar para la barra de progreso
    

#solucion_incumbente = 
#peso_incumbente = 
#print(f"\n Solución incumbente: {solucion_incumbente} \n")
#print(f"peso incumbente: {peso_incumbente} \n")

# gráfico de mejoramiento de función objetivo
#fig = px.line(historia_incumbente)
#fig.show()