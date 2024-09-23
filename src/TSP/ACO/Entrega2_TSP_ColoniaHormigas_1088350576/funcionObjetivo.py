import numpy as np

def funcionObjetivo(solucion,dist,numero_clientes): # -> float:
    # Calcula la funcion objetivo de una solucion
    F_obj:float = 0
    #NumClientes:int = 
    for arco in range(numero_clientes):
        F_obj += dist[solucion[arco],solucion[arco+1]]
    return F_obj

#Prueba
if __name__ == "__main__":
    # matriz de distancias
    dist = np.array([[0,1,2,3,4],[1,0,1,2,3],[2,1,0,1,2],[3,2,1,0,1],[4,3,2,1,0]])
    # solución
    solucion = np.array([0,1,2,3,4,0])
    # número de clientes
    numero_clientes = 5
    print(funcionObjetivo(solucion,dist,numero_clientes))