import numpy as np
from funcionObjetivo import funcionObjetivo

def busquedaLocal(circuitos,dist,longitud_tours,n): # -> tuple[np.ndarray,np.ndarray]:
    
    # array del mismo tamaño que circuitos para guardar las soluciones mejoradas de cada circuitos
    soluciones:np.ndarray = np.zeros(np.shape(circuitos),dtype=int)
    
    #Or- OPT
    k:int = 0
    for solucion in circuitos:
        # S0 como valor de función objetivo inicial
        S0 = funcionObjetivo(solucion,dist,n)
        
         # Tamaño de las soluciones (usado para recorrerlas en los ciclos for)
        size=np.shape(solucion)[0]
        
         # definir la variable solucion_incumbente desde la primer solución (instancias o copiar)
        solucion_mejorada = solucion.copy()
         # iterar para realizar los intercambios intra-ruta. Tener en cuenta que el inicio y fin no se modifican
        for i in range(1,size-1):
            for j in range(1,size-1):
                if i!=j:
                    solucion_prueba = solucion.copy() # solución temporal para hacer intercambios
                    solucion_prueba[j] = solucion[i]  # inserción de cliente i en posición j
                    solucion_prueba[i] = solucion[j] # inserción de cliente j en posición i
                    S1 = funcionObjetivo(solucion_prueba,dist,n)
                    if S1<S0:
                        S0=S1
                        solucion_mejorada = solucion_prueba.copy()  
        soluciones[k,:] = solucion_mejorada # solución mejorada
        longitud_tours[k] = S0  # valor función objetivo de solución mejorada
        k +=1    
        
    return soluciones,longitud_tours