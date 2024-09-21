import numpy as np
from bin_pack_bl import bin_pack_bl
from generar_vecino import generar_vecino

def temperatura_inicial(perturbaciones,vecino_actual,bin_capacity,funcion_objetivo_inicial,tao): # -> float:
    
    m1:int= 0  # contador de vecinos de mejor calidad
    m2:int = 0  # contador de vecinos de peor calidad
    deltaE:float = 0 # Valor promedio de las transiciones que degradaron la función objetivo
    delta_total:float = 0 # Valor acumulado del delta equivalente a la suma acumulada de la función objetivo que no mejora
    
    # iniciar las perturbaciones
    for i in range(perturbaciones):
        vecino = generar_vecino(vecino_actual)      # generar vecino
        funcion_objetivo_vecino,_, _ = bin_pack_bl(vecino, bin_capacity)
        if funcion_objetivo_vecino > funcion_objetivo_inicial: #maximizando
            # contar los mejoramientos
            m1 += 1
        else:
            m2 = m2 + 1
            delta_total = delta_total + funcion_objetivo_vecino
    deltaE = delta_total / m2

    # calcular la temperatura inicial. Se usa try-except para evitar división por cero
    try:
        initial_temperature = deltaE / np.log(m2/(m2*tao-m1*(1-tao)))
    except:
        initial_temperature = deltaE / np.log(m2/(m2*tao-m1*(1-tao))) + 1e-10 # suma de valor pequeño en denominador para evitar division por cero
    
    return initial_temperature

