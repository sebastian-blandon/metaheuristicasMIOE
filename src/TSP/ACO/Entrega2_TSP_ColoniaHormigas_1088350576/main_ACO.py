import numpy as np
from cargar_datos import cargar_datos
from distancias import distancias
from construir_soluciones import construir_soluciones
from busquedaLocal import busquedaLocal
from actualizarFeromona import actualizarFeromona
from tqdm import tqdm
import plotly.express as px
import plotly.graph_objects as go
import random

# Establecer semilla aleatoria
random.seed(0)
np.random.seed(0)

# Cargar datos
coordenadas = cargar_datos()

# Número de clientes
n:int = len(coordenadas)

# Parametros algoritmo ACO
m:int = 10 #Número de hormigas. Debe ser menor al número de clientes n
bl:int = 10 #Número de búsquedas locales
Cnn:int = 1000 #Longitud inicial del circuito
alpha:int = 1 #Importancia relativa de depositos de feromona
beta:int = 5 #Importancia relativa de los nodos más cercanos
rho:float = 0.1 #Factor de evaporación
Tao:np.ndarray = np.ones((n,n)) * m / Cnn #matriz de feromonas nxn (clientes)
iterMax:int = 100 #Número máximo de iteraciones
pbar = tqdm(total=iterMax)

dist:np.ndarray = distancias(coordenadas) # Matriz de distancias

# inicializar matriz Matriz_longitud_tours (históricos de función objetivo)
Matriz_longitud_tours = np.zeros((iterMax,2)) # Guarda el historico

# incumbente inicial: valor infinito (minimización)
incumbente:float = 1000000000000000000

k = 0 # contador de inserción de incumbentes
for i in range(iterMax):
    pbar.update()

    #Construir soluciones
    circuitos,longitud_tours = construir_soluciones(Tao,dist,m,n,alpha,beta)
    soluciones,longitud_tours = busquedaLocal(circuitos,dist,longitud_tours,n)
    
#    # Verificar si hay mejoramiento
    if np.min(longitud_tours) < incumbente:
        incumbente = np.min(longitud_tours)
        indice_mejor_solucion = np.argmin(longitud_tours)
        solucion_incumbente = soluciones[indice_mejor_solucion]
        
        
        Matriz_longitud_tours[k,0] = i
        Matriz_longitud_tours[k,1] = incumbente
        k += 1

    Tao = actualizarFeromona(Tao,rho,soluciones,longitud_tours,m,n)

pbar.close()

# Eliminar ceros de Matriz_longitud_tours
mask = Matriz_longitud_tours[:, 1] != 0  # Check for non-zero in the first column
Matriz_longitud_tours = Matriz_longitud_tours[mask]

print("\n Solución:",solucion_incumbente)
print("\n Longitud:", incumbente)

# Graficar evolución de las solucines encontradas
fig = px.line(x=Matriz_longitud_tours[:,0],y=Matriz_longitud_tours[:,1])
fig.show()

# Graficar solución
x = coordenadas[solucion_incumbente,0]
y = coordenadas[solucion_incumbente,1]
text_labels = list(map(str, solucion_incumbente))
# Generar los trazos
trace1 = go.Scatter(x=x, y=y, mode='lines')
trace2 = go.Scatter(x=x+0.8, y=y+0.8, mode='text',text=text_labels)
fig = go.Figure(data=[trace1, trace2])
fig.show()