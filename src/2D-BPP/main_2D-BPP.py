import numpy as np
from bin_pack_bl import bin_pack_bl
from numpy import ndarray
from generar_vecino import generar_vecino_inicial, generar_vecino
from plot_bin_packing_bl import plot_bin_packing_bl
from temperatura_inicial import temperatura_inicial
from metropolis import metropolis
import random
from tqdm import tqdm

#### iniciar problema con función button-left ####
semilla = 100
np.random.seed(semilla)
random.seed(semilla)


#dims:ndarray = np.array([[4, 6], [2, 8], [5, 3], [7, 2]])
dims = np.random.randint(1, 8, size=[10,2])
print(dims)
solucion_inicial,matriz_solucion = generar_vecino_inicial(dims, semilla)
bin_capacity = [20, 20]

# Obtener función objetivo solución inicial
packed_bin = bin_pack_bl(solucion_inicial, bin_capacity)

#gráficar solución inicial
plot_bin_packing_bl(bin_capacity, packed_bin)

# mostrar datos de solución inicial: obtenerlos desde la variable <packed_bin>. usable_empty_space_Area,occupied_area, item_placements
usable_empty_space_Area,occupied_area, item_placements = packed_bin

print(f"Bin: Occupied Area = {occupied_area}, usable empty space Area = {usable_empty_space_Area}, Item Placements = {item_placements}")


#########################################################################################################


#### Definición de parámetros de algoritmo simulated annealing ####

tao:float  = 0.8 # tasa de aceptación de vecinos
stopping_condition:int = 100 # número de iteraciones para alcanzar la temperatura final
cooling_rate:float  = 0.97 # factor de ajuste de temperatura o tasa de enfriamiento
perturbaciones:int  = 100 # número de perturbaciones a la temperatura
rho:int = dims.shape[0] * dims.shape[1] # Longitud de cadena de markov
beta:float = 1.01 # factor de ajuste de rho

# función objetivo
vecino_actual =  solucion_inicial      # como solución inicial
funcion_objetivo_actual:int = usable_empty_space_Area

incumbente = {
    "funcion_objetivo": funcion_objetivo_actual,
    "solucion": vecino_actual
}

# calculo de temperatura inicial
temperatura_actual:float = temperatura_inicial(
                                            perturbaciones,
                                            vecino_actual,
                                            bin_capacity,
                                            funcion_objetivo_actual,
                                            tao)

#### inicio de iteraciones del simulated annealing ####
contIter = 0
with tqdm(total=stopping_condition) as pbar:
    while contIter < stopping_condition:           # bucle de criterio de terminación
        k = 0      # contador de cambios de estados de energía
        while k < rho:   # bucle de cambio de estado de energía. Verificación de k con respecto al valor de la cadena de markov
            k += 1
            vecino_alternativa = generar_vecino(solucion_inicial)
            funcion_objetivo_alternativa,_, _ = bin_pack_bl(vecino_alternativa, bin_capacity)
            
            # regla de aceptación de metropolis
            vecino_actual, funcion_objetivo_actual, incumbente, contIter = metropolis(vecino_actual,
                                                                                    vecino_alternativa,
                                                                                    funcion_objetivo_actual,
                                                                                    funcion_objetivo_alternativa,
                                                                                    temperatura_actual,
                                                                                    incumbente,
                                                                                    contIter)
        rho = int(beta * rho)
        temperatura_actual = cooling_rate * temperatura_actual
        contIter += 1  # contador de iteraciones

        incum = incumbente['funcion_objetivo']
        pbar.set_description(f"fo_Incumbente: {incum}")
        pbar.update()

print(incumbente)

# Plot the first bin 
packed_bin = bin_pack_bl(incumbente['solucion'], bin_capacity)
plot_bin_packing_bl(bin_capacity, packed_bin)



