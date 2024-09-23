import numpy as np


def metropolis(vecino_actual,vecino_alternativa,funcion_objetivo_actual,funcion_objetivo_alternativa,temperatura_actual,incumbente,contIter):
    
    # condicional que acepta el vecino alternativo si es mejor que el actual
    if funcion_objetivo_alternativa > funcion_objetivo_actual: 
        funcion_objetivo_actual = funcion_objetivo_alternativa
        vecino_actual = vecino_alternativa.copy()
    else:
        prob_alternativa:float = np.exp(-(funcion_objetivo_actual - funcion_objetivo_alternativa) / temperatura_actual)
        aleatorio:float = np.random.rand()
        if aleatorio <= prob_alternativa: # acepta vecino segun probabilidad que depende de la temperatura actual
            # actualiza
            vecino_actual = vecino_alternativa.copy()
            funcion_objetivo_actual = funcion_objetivo_alternativa
    
    # Actualizar incumbente        
    if funcion_objetivo_actual > incumbente["funcion_objetivo"]:
        incumbente["funcion_objetivo"] = funcion_objetivo_actual
        incumbente["solucion"] = vecino_actual
        #contIter = 0
    
    return vecino_actual, funcion_objetivo_actual, incumbente, contIter