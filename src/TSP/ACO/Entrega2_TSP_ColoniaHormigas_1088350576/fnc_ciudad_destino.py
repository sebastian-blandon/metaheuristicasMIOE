import numpy as np

def fnc_ciudad_destino(candidato_destino:int,
                   M:np.ndarray,
                   ciudad_inicial:int,
                   n:int,
                   Tao:np.ndarray,
                   alpha:float,
                   beta:float,
                   dist: np.ndarray
                   ): #-> int:
    
    # calculo del denominador de la función de probabilidad
    # inicializar vector de probabilidad con tamaño n.
    probabilidad:np.ndarray = np.zeros(n)
    denominador:float = 0.0
    for i in range(n): # Bucle para calcular la sumatoria del denominador
        #verificar matriz de ciudades visitadas y que i no sea la ciuidad de inicio del arco.
        if  M[candidato_destino,i] == 0 and i != ciudad_inicial:
            denominador = denominador + (Tao[ciudad_inicial,i]**alpha * (1/dist[ciudad_inicial,i])**beta)
      
    
          
    # cálculo de la probabilidad (numerador y probabilidad)
    # la variable ciudad_no_visitada almacena los candidatos de ciudades a visitar
    ciudad_no_visitada:np.ndarray = np.zeros(n) # Inicializar variable
    
    contador:int = 0
    for j in range(n):
     #   verificar matriz de ciudades visitadas y que j no sea la ciudad de inicio del arco.
        if M[candidato_destino,j] == 0 :
            numerador:float = (Tao[ciudad_inicial,j]**alpha * (1/dist[ciudad_inicial,j])**beta)
            probabilidad[contador] = numerador/denominador
            ciudad_no_visitada[contador] = j
            contador += 1
    
    # remover espacios no usados (ceros)
    ciudad_no_visitada = ciudad_no_visitada[0:contador]
    probabilidad = probabilidad[0:contador]
    
    # seleccion de la ciudad destino
    ciudad_destino :int= int(np.random.choice(ciudad_no_visitada, p=probabilidad))
    
    return ciudad_destino
            

    
        