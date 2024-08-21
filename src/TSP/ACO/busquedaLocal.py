import numpy as np
from funcionObjetivo import funcionObjetivo

def busquedaLocal(circuitos,dist,longitud_tours): # -> tuple[np.ndarray,np.ndarray]:
    
    # array del mismo tamaño que circuitos para guardar las soluciones mejoradas de cada circuitos
    #soluciones:np.ndarray= 
    
    #Or- OPT
    k:int = 0
    #for solucion in circuitos:
    #    # S0 como valor de función objetivo inicial
    #    S0 = funcionObjetivo(solucion,dist)
    #    
         # Tamaño de las soluciones (usado para recorrerlas en los ciclos for)
    #    size=np.shape(solucion)
        
         # definir la variable solucion_incumbente desde la primer solución (instancias o copiar)
    #    solucion_incumbente = 
         
         # iterar para realizar los intercambios intra-ruta. Tener en cuenta que el inicio y fin no se modifican
    #    for i in range(XXXX,XXXX):
    #        for j in range(XXXX,XXXX):
    #            if i!=j:
    #                solucion_prueba =      # solución temporal para hacer intercambios
    #                solucion_prueba[j] =   # inserción de cliente i en posición j
    #                solucion_prueba[i] =   # inserción de cliente j en posición i
    #                S1 = funcionObjetivo(solucion_prueba,dist)
    #                if S1<S0:
    #                    S0=S1
    #                    solucion_incumbente = 
    #                    
    #                
    #    soluciones[k,:] =      # solución mejorada
    #    longitud_tours[k] =    # valor función objetivo de solución mejorada
    #    k +=1    
        
    return #soluciones,longitud_tours