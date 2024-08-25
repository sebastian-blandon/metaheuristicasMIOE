import numpy as np

def funcion_objetivo(hijos,precio_objetos,peso_objetos,peso_maximo):

    # inicializa variables como listas vacias (también puede usar numpy)
    func_obj = []
    peso_actual = []
    
    # llenado de variables. Iterar sobre los hijos. 
    # La función objetivo es la sumatoria de la multiplicación de los vectores hijo y precio_objetos
    for hijo in hijos:
        func_obj.append(np.sum(hijo*precio_objetos))
        peso_actual.append(np.sum(hijo*peso_objetos))
    
    # penalizar valores mayores a peso_maximo obtenidos después del cruzamiento entre padres
    # Se incluye proporcion para el concepto de adaptacion
    for i in range(len(func_obj)):
        if peso_actual[i] > peso_maximo:
            proporcion_desfase = (peso_actual[i]-peso_maximo)/peso_maximo
            
            # incluir un multiplicador el excedente de peso sobrepasado para penalizar la función objetivo
            func_obj[i] = func_obj[i] - (func_obj[i]*proporcion_desfase)

    
    return func_obj,peso_actual


if __name__=="__main__":
    individuos = np.array([[1,0,1,0,1],[0,0,1,0,1]])
    precio_objetos = np.array([10,20,30,40,50])
    peso_objetos = np.array([1,2,3,4,5])
    peso_maximo = 10
    func_obj,peso_actual = funcion_objetivo(individuos,precio_objetos,peso_objetos,peso_maximo)
    print("func_obj:",func_obj)
    print("peso_actual:",peso_actual)