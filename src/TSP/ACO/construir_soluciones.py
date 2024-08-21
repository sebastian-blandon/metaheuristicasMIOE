import numpy as np
from fnc_ciudad_destino import fnc_ciudad_destino
from funcionObjetivo import funcionObjetivo

def construir_soluciones(Tao,dist,m,n,alpha,beta): # -> tuple[np.ndarray, np.ndarray]:
    
    #Matriz de ciudades visitadas mxn
    #M:np.ndarray = 
    paso:int = 0 # inicio de los pasos de la hormiga
    #circuitos:np.ndarray = 
    
    #Seleccion de la ciudad inicial de cada hormiga

    #Nodos iniciales de las hormigas como permutación aleatoria
    #r:np.ndarray = 
    # inicio los circuitos
    #circuitos[:, 0] = r
    
    # actualiza matriz de ciudades visitadas. 1: si fue visitada; 0: si no ha sido visitada
    #for i in range(m):
    #    M[i, r[i]] = 
    
    #Seleccion de la siguiente ciudad de cada hormiga
    #while paso < n-1:
    #    paso += 1
    #    for i in range(m):
            #ciudad_inicial = int(XXXXX)
            #ciudad_destino:int = fnc_ciudad_destino(i,M,ciudad_inicial,n,Tao,alpha,beta,dist)
            #circuitos[i, paso] =       # asignar la ciudad destino en el circuito i del correspondiente paso
            
            # actualiza matriz de ciudades visitadas
            #M[i, ciudad_destino] = 
    
    
    # ciudad para hacer el retorno al inicio del circuito
    ### su código va aquí ###
        
    #computar longitud de cada tour
    #longitud_tours:np.ndarray =        # inicializa variable
    #for i in range(m):
    #    longitud_tours[i] = funcionObjetivo(circuitos[i,:],dist)

    return #circuitos,longitud_tours