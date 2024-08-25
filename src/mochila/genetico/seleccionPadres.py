import numpy as np

def seleccionPadres(k,funcion_objetivo_pop,poblacion_inicial,tamanio_poblacion): # Eliminar número de objetos, revisar dónde se está utilizando

    indices_candidatos =  np.random.permutation(tamanio_poblacion)# como una permutación aleatoria usando numpy
    
    # construir tabla candidatos: columna uno indices candidatos aleatorios, columna dos sus FO
    tabla_candidatos = np.zeros((tamanio_poblacion,2), dtype=int)  # inicializar
    tabla_candidatos[:, 0] = indices_candidatos      # indexar
    tabla_candidatos[:, 1] = funcion_objetivo_pop[indices_candidatos] # Se indexa para que cargue las funciones objetivos correspondientes a cada indice de candidatos

    # seleccion de k candidatos
    muestra = tabla_candidatos[0:k,:]
    #print("muestra \n", muestra)
    
    # ordendar la muestra de mayor a menor por función objetivo
    #muestra = tabla_candidatos.sort_values(by='funcion_objetivo_pop', asceding=FALSE)
    muestra  = muestra[muestra[:,1].argsort()[::-1]] # Revisar la lógica, el profe lo generó con copilot

    # obtener a los padres desde la población usando los indices de la muestra
    #padre_1 = poblacion_inicial["filas que quiero", "columnas que quiero"]
    indice_padre_1 = muestra[0][0] # El primero determina la fila y el segundo la columna
    indice_padre_2 = muestra[1][0]
    padre_1 = poblacion_inicial[indice_padre_1, :]
    padre_2 = poblacion_inicial[indice_padre_2, :]

    #print("padre_1 \n", padre_1)
    #print("padre_2 \n", padre_2)
    padres = np.array([padre_1, padre_2])
    
    return padres
    



# Prueba
if __name__=="__main__":
    funciones_objetivo = np.array([10,20,30,40,50,60,70,80,90,100])
    poblacion_inicial = np.array([[1,0,1,0,1],[0,0,1,0,1],[1,0,1,0,1],[0,0,1,0,1],[1,0,1,0,1],[0,0,1,0,1],[1,0,1,0,1],[0,0,1,0,1],[1,0,1,0,1],[0,0,1,0,1]])
    tamano_poblacion = 10
    numero_objetos = 5
    candidatos = 3
    padres = seleccionPadres(candidatos,funciones_objetivo,poblacion_inicial,tamano_poblacion,numero_objetos)
    print("padres:",padres)
    print("shape padres:",padres.shape)
    print("type padres:",type(padres))
    print("shape esperado:",(2,5))
    print("type esperado:",np.ndarray)