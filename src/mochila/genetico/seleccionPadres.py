import numpy as np

def seleccionPadres(k,funcion_objetivo_pop,poblacion_inicial,tamanio_poblacion,numero_objetos):

    indices_candidatos =  np.random.permutation(tamanio_poblacion)# como una permutación aleatoria usando numpy
    
    # construir tabla candidatos: columna uno indices candidatos aleatorios, columna dos sus FO
    tabla_candidatos = np.zeros((tamanio_poblacion,2))  # inicializar
    tabla_candidatos[:, 0] = indices_candidatos      # indexar
    tabla_candidatos[:, 1] = funcion_objetivo_pop      # indexar

    # seleccion de k candidatos
    #muestra = tabla_candidatos[0:"cantidad candidatos",:]
    
    # ordendar la muestra de menor a mayor por función objetivo
    #muestra = 

    # obtener a los padres desde la población usando los indices de la muestra
    #padre_1 = 
    #padre_2 = 

    #padres = np.array([padre_1, padre_2])
    
    return #padres
    



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