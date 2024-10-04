import numpy as np


def poblacion_inicial(tamanio_poblacion,numero_ciudades):

    # inicializar matriz de población como un array de numpy
    poblacion_inicio = np.zeros((tamanio_poblacion, numero_ciudades), dtype=int)
    i = 0
    while i < tamanio_poblacion: #generación de rutas aleatorias: permutacion de ciudades
        #individuo = np.random.permutation(numero_ciudades) # Esto es un vector
        individuo = np.random.randint(0,2, numero_ciudades) # Esto es un vector
        # Agregar la ruta a la poblacion
        poblacion_inicio[i] = individuo

        # Verificar si el individuo es factible
        # No es necesario verificar factibilidad, porque no estoy delimitando una distancia maxima recorrida
        i+=1

    return poblacion_inicio

 # Test funcion
tamanio_poblacion = 10
numero_ciudades = 26

retorno = poblacion_inicial(tamanio_poblacion,numero_ciudades)
print(retorno)