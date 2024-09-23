import numpy as np
from fnc_ciudad_destino import fnc_ciudad_destino
from funcionObjetivo import funcionObjetivo

def construir_soluciones(Tao,dist,m,n,alpha,beta): # -> tuple[np.ndarray, np.ndarray]:
    
    #Matriz de ciudades visitadas mxn
    M:np.ndarray = np.zeros((m,n))
    paso:int = 0 # inicio de los pasos de la hormiga
    # El valor de las columnas es n+1, porque incluyo el retorno al inicio
    circuitos:np.ndarray = np.zeros((m,n+1), dtype=int)
    
    #Seleccion de la ciudad inicial de cada hormiga

    #Nodos iniciales de las hormigas como permutación aleatoria
    r:np.ndarray = np.random.permutation(m) # Todas las hormigas inician en puntos diferentes
    # inicio los circuitos
    circuitos[:, 0] = r # En todas las filas se pone el vector r en la primera fila
    print("")
    
    # actualiza matriz de ciudades visitadas. 1: si fue visitada; 0: si no ha sido visitada
    for i in range(m):
        M[i, r[i]] = 1 # REVISAR, NO LO ENTENDÍ
    
    #Seleccion de la siguiente ciudad de cada hormiga
    while (paso < n-1):
        paso += 1
        # Bucle for para encontrar la ciudad destino de cada hormiga
        for i in range(m):
            # Ciudad inicial corresponde a la ciudad visitada en la iteración anterior
            ciudad_inicial = int(circuitos[i,paso-1])
            ciudad_destino:int = fnc_ciudad_destino(i,M,ciudad_inicial,n,Tao,alpha,beta,dist)
            circuitos[i, paso] = ciudad_destino # asignar la ciudad destino en el circuito i del correspondiente paso
            
            # actualiza matriz de ciudades visitadas
            M[i, ciudad_destino] = 1
    
    
    # ciudad para hacer el retorno al inicio del circuito
    circuitos[:,n] = circuitos[:,0]
        
    #computar longitud de cada tour
    longitud_tours:np.ndarray = np.zeros(m)       # inicializa variable
    for i in range(m):
        longitud_tours[i] = funcionObjetivo(circuitos[i,:],dist,n)

    return circuitos,longitud_tours