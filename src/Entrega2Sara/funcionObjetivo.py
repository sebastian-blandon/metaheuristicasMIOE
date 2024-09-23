import numpy as np

def funcionObjetivo(solucion,dist,numero_clientes): # -> float:
    # Calcula la funcion objetivo de una solucion

    F_obj:float = 0    
    for arco in range(numero_clientes): #La cantidad de arcos es igual al número de nodos porque incluye el arco de retorno
       F_obj += dist[solucion[arco],solucion[arco+1]] #(F_onj = F_obj) = (F_obj +=)
        
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