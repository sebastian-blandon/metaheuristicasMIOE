import numpy as np

# Generar una funcion que calcule la sumatoria de la multiplicacion del vector poblacion_inicial y la distancia entre ellas
def funcion_objetivo_pop(poblacion,matriz_distancias):
    # Inicializar variable distancia
    distancia_recorrida = np.zeros(len(poblacion))
    # Iterar sobre la poblacion
    for i in range(len(poblacion)):
        # Iterar sobre la distancia entre las ciudades
        for j in range(len(poblacion[i])):
            distancia_recorrida[i] += (poblacion[i][j]*matriz_distancias[i][j])
    return distancia_recorrida
# REVISAR ESA FUNCION POP


def funcion_objetivo(hijos,matriz_distancias,incumbente_inicial):

    # inicializa variables como listas vacias (también puede usar numpy)
    func_obj = []
    
    # llenado de variables. Iterar sobre los hijos. 
    for hijo in hijos:
        func_obj.append(funcion_objetivo_pop(hijo,matriz_distancias))
    
    # penalizar valores mayores a peso_maximo obtenidos después del cruzamiento entre padres
    # Se incluye proporcion para el concepto de adaptacion
    for i in range(len(func_obj)):
        if func_obj[i] > incumbente_inicial:
            proporcion_desfase = (func_obj[i]-incumbente_inicial)/incumbente_inicial
            
            # incluir un multiplicador para penalizar la función objetivo
            func_obj[i] = func_obj[i] - (func_obj[i]*proporcion_desfase)

    
    return func_obj


if __name__=="__main__":
    individuos = np.array([[1,0,1,0,1],[0,0,1,0,1]])
    precio_objetos = np.array([10,20,30,40,50])
    peso_objetos = np.array([1,2,3,4,5])
    peso_maximo = 10
    func_obj,peso_actual = funcion_objetivo(individuos,precio_objetos,peso_objetos,peso_maximo)
    print("func_obj:",func_obj)
    print("peso_actual:",peso_actual)