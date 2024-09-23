import numpy as np

def distancias(coordenadas:np.ndarray) -> np.ndarray:
    
    n = len(coordenadas) #Número de objetos
    # inicializar matriz de distancias
    matriz_distancia:np.ndarray = np.zeros((n,n))
    
    # doble bucle for para indexación de matriz
    for i in range(n):
        for j in range(n):
            if i!=j:
                matriz_distancia[i][j] = np.sqrt((coordenadas[i,0] - coordenadas[j,0])**2 + (coordenadas[i,1] - coordenadas[j,1])**2)
            
         
    
    
    return matriz_distancia

#Prueba

if __name__ == "__main__": 
    coordenadas = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
    print(distancias(coordenadas))