import numpy as np


def poblacion_inicial(tamanio_poblacion,numero_objetos,peso_maximo_mochila,peso_objetos):

    # inicializar matriz de población como un array de numpy
    poblacion_inicio = np.zeros((tamanio_poblacion, numero_objetos), dtype=int)
    i = 0
    while i < tamanio_poblacion: #generación de individuos aleatorios: vector con rutas aleatorias
        individuo = np.random.randint(0,2, numero_objetos) # Esto es un vector
        # obtener el peso del individuo
        peso_individuo = np.sum(individuo*peso_objetos)


        # Verificar si el individuo es factible
        if peso_individuo < peso_maximo_mochila:
            poblacion_inicio[i] = individuo


            i+=1

    return poblacion_inicio

# # Test funcion
# tamanio_poblacion = 10
# numero_objetos = 30
# peso_maximo_mochila = 500
# peso_maximo_objeto = 50
# precio_maximo = 100
# peso_objetos = np.random.randint(1, peso_maximo_objeto, numero_objetos)

# retorno = poblacion_inicial(tamanio_poblacion,numero_objetos,precio_maximo,peso_objetos)
# print(retorno)
