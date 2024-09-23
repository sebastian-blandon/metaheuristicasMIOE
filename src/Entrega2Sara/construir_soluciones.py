import numpy as np
from fnc_ciudad_destino import fnc_ciudad_destino
from funcionObjetivo import funcionObjetivo

def construir_soluciones(Tao,dist,m,n,alpha,beta): # -> tuple[np.ndarray, np.ndarray]:
    
    #Matriz de ciudades visitadas mxn
    M:np.ndarray = np.zeros((m,n))

    paso:int = 0 # inicio de los pasos de la hormiga

    #El valor de las columnas n+1 porque incluye la ciudad de retorno, vuelve al inicio
    circuitos:np.ndarray = np.zeros((m,n+1), dtype=int)
    
    #Seleccion de la ciudad inicial de cada hormiga

    #Nodos iniciales de las hormigas como permutación aleatoria
    #Los circuitos son mis soluciones actuales
    r:np.ndarray = np.random.permutation(m)
    # inicio los circuitos
    circuitos[:, 0] = r  #todas las filas en la columa 0 me ponga el vector r
    print("")
    
    # actualiza matriz de ciudades visitadas. 1: si fue visitada; 0: si no ha sido visitada
    for i in range(m):
        M[i, r[i]] = 1
  
    #Seleccion de la siguiente ciudad de cada hormiga
    while paso < n-1:
        paso += 1
        #blucle for para encontrar la ciudad destino de cada hormiga
        for hormiga in range(m): 
            #Ciudad inicial corresponde a la ciudad en la ietración anterior
            ciudad_inicial = int(circuitos[hormiga, paso-1])
            ciudad_destino:int = fnc_ciudad_destino(hormiga,M,ciudad_inicial,n,Tao,alpha,beta,dist)
            circuitos[hormiga, paso] = ciudad_destino      # asignar la ciudad destino en el circuito i del correspondiente paso
            
        
            # actualiza matriz de ciudades visitadas
            M[hormiga, ciudad_destino] = 1
    
    
    # ciudad para hacer el retorno al inicio del circuito
    circuitos[:,n] = circuitos[:,0]
   
    #computar longitud de cada tour
    longitud_tours:np.ndarray =  np.zeros(m)    # inicializa variable
    for hormiga in range(m): 
        longitud_tours[hormiga] = funcionObjetivo(circuitos[hormiga,:],dist,n)

    return circuitos,longitud_tours