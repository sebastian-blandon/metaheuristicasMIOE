import numpy as np

def distancias(coordenadas:np.ndarray)-> np.ndarray:
    
    # Número de clientes
    n:int = len(coordenadas)

    # inicializar matriz de distancias
    distancia:np.ndarray = np.zeros((n,n))
    
    # doble bucle for para indexación de matriz
    for i in range(n):
        for j in range(n):
            if i==j:
                distancia[i,j] = 0
            else:
                distancia[i,j] = np.sqrt((coordenadas[i,0] - coordenadas[j,0])**2 + (coordenadas[i,1] - coordenadas[j,1])**2)
                #distancia[i][j] = np.linalg.norm(coordenadas[i] - coordenadas[j])
    return distancia


# Prueba de la funcion distancia

if __name__ == "__main__": 
    coordenadas = np.array([[0, 0], [1, 1], [2, 2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8], [9,9]])
    print(distancias(coordenadas))