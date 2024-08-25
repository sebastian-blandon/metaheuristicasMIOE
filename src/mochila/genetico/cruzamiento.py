import numpy as np


def cruzamiento(padres):

    padre_1 = padres[0]
    padre_2 = padres[1]

    num_elementos = len(padre_1) # numero de elementos vector

    # generación de cortes aleatorios para cruzamiento
    while True:
        corte_1 = np.random.randint(0, num_elementos-1) # -1 para evitar desbordamiento
        corte_2 = np.random.randint(0, num_elementos-1) # -1 para evitar desbordamiento
        if corte_1 < corte_2:
            break

    #print(f"Corte 1: {corte_1}")
    #print(f"Corte 2: {corte_2}")
    
    # inicialización de las variables hijos
    hijo_1 = np.zeros((num_elementos), dtype = int)
    hijo_2 = np.copy(hijo_1)


    # llenado de partes exteriores de los cortes con padres e hijos iguales
    hijo_1[0:corte_1+1] = padre_1[0:corte_1+1]
    hijo_1[corte_2+1:] = padre_1[corte_2+1:]

    hijo_2[0:corte_2+1] = padre_2[0:corte_2+1]
    hijo_2[corte_2+1:] = padre_2[corte_2+1:]
    
    #hijo_1[X:XXXX] =

    #hijo_2[X:XXXX] = 
    #hijo_2[X:XXXX] = 

    # llenado de partes interiores de los cortes con padres e hijos cruzados
    #hijo_1[XXXX:XXXX] = 
    hijo_1[corte_1+1:corte_2+1] = padre_2[corte_1+1:corte_2+1] # Revisar porqué se suma 1
    #hijo_2[XXXX:XXXX] =
    hijo_2[corte_1+1:corte_2+1] = padre_1[corte_1+1:corte_2+1]
    
    #hijos = np.array([hijo_1, hijo_2])
    hijos = np.array([hijo_1, hijo_2])

    #return #hijos
    #return corte_1, corte_2
    return hijos

 
# test funcion cruzamiento
if __name__ == "__main__":
    padre_1 = np.array([1, 2, 3, 4, 5])
    padre_2 = np.array([6, 7, 8, 9, 10])
    padres = np.array([padre_1, padre_2])
    hijos = cruzamiento(padres)
    print(hijos)

