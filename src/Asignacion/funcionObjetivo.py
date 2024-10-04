import numpy as np

def funcionObjetivo(solucion:np.ndarray, costos:np.ndarray)->int:
    
    # inicializar variable costo
    costo:int = 0
    
    # inicializar recorrido en el vector solución para obtener su costo acumulado
    numero_tareas = len(solucion)
    for tarea in range(numero_tareas):
        costo += costos[solucion[tarea],tarea]
    
    return costo # variable de retorno