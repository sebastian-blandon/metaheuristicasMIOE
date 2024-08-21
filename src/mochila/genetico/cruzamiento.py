import numpy as np


def cruzamiento(padres):

    padre_1 = padres[0]
    padre_2 = padres[1]

    num_elementos = len(padre_1) # numero de elementos vector

    # generación de cortes aleatorios para cruzamiento PMX
    #while True:
    #    corte_1 = 
    #    corte_2 = 
    #    if corte_1 < corte_2:
    #        break
    
    # inicialización de las variables hijos
    #hijo_1 = 
    #hijo_2 = 

    # llenado de partes exteriores de los cortes con padres e hijos iguales
    #hijo_1[X:XXXX] =
    #hijo_1[X:XXXX] =

    #hijo_2[X:XXXX] = 
    #hijo_2[X:XXXX] = 

    # llenado de partes interiores de los cortes con padres e hijos cruzados
    #hijo_1[XXXX:XXXX] = 
    #hijo_2[XXXX:XXXX] =
            
    #hijos = np.array([hijo_1, hijo_2])

    return #hijos

 
# test funcion cruzamiento
if __name__ == "__main__":
    padre_1 = np.array([1, 2, 3, 4, 5])
    padre_2 = np.array([6, 7, 8, 9, 10])
    padres = np.array([padre_1, padre_2])
    hijos = cruzamiento(padres)
    print(hijos)
            
    