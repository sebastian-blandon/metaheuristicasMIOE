import numpy as np


def actualizarFeromona(Tao:np.ndarray,
                       rho:float,
                       circuitos:np.ndarray,
                       longitud_tours:np.ndarray,
                       m:int,
                       n:int
                       ) -> np.ndarray:
    #evaporación feromona (formulación de la tasa de evaporación)
    #Tao = 
    
    #actualizar feromona para cada hormiga m
    #for i in XXXXX: #recorre circuitos
    #    delta:       #aumento proporcional a la calidad del circuito
    #    for j in XXXXX: #recorre clientes o ciudades
    #        # obtener el nodo de inicio "k" y el nodo destino "l" en la ruta i
    #        cliente_k =  #cliente k de la ruta i
    #        cliente_l =  #cliente l de la ruta i
    #        
    #        # indexa el valor de Tao
    #        Tao[XXXX,XXXXX] += 
    #        
    #    # actualizar feromona para la ultima ciudad del circuito (requerido ya que el arco de retorno es una abstracción en el vecto de solución)
    #    cliente_k = 
    #    cliente_l = 
    #    Tao[XXXXX] += 
    
    return Tao