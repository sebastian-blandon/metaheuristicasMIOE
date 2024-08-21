import numpy as np


def opt_operator(vecino:np.ndarray,memoria_tabu:np.ndarray): #-> tuple[np.ndarray,tuple[int,int]]:
    
    # inicializar varibles indice_1 y indice_2
    #indice_1:int = 0
    #indice_2:int = 0
    # inicializar variable no_es_tabu como bool
    #no_es_tabu:bool = 
    
    # bucle para generar 2 indices que no son tabu
    #while indice_1 == indice_2 and no_es_tabu:
        #selecionar 2 posiciones aleatorias
        #indice_1 = 
        #indice_2 = 
        # actualizar variable <no_es_tabu>. Si en memoria_tabu hay un valor mayor que cero, el movimiento es tabu.
        # ayuda: se puede usar el operador booleano "not" que evalua si hay un dato. Si lo hay es "True", si es cero devuelve "False"
        #no_es_tabu:bool = 
    
    #movimiento:tuple = 
    #intercambiar las posiciones
    #nuevo_vecino:np.ndarray = vecino.copy()
    #nuevo_vecino[X] = 
    #nuevo_vecino[Y] = 

    return #nuevo_vecino,movimiento



#prueba de la funcion opt_operator
if __name__ == "__main__": 
    solucion = np.array([0, 1, 2])
    movimientos_candidatos = np.array([[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]])
    memoria_tabu = np.zeros((len(solucion), len(solucion)), dtype=bool)
    print(opt_operator(solucion,memoria_tabu))
    