import numpy as np


def actualizarFeromona(Tao:np.ndarray,
                       rho:float,
                       soluciones:np.ndarray,
                       longitud_tours:np.ndarray,
                       m:int,
                       n:int
                       ) -> np.ndarray:
    #evaporación feromona (formulación de la tasa de evaporación)
    Tao = (1-rho) * Tao
    
    #actualizar feromona para cada hormiga m
    for i in range(m): #recorre circuitos
        delta:float = 1/longitud_tours[i]  #aumento proporcional a la calidad del circuito
        for cliente in range(n-1): #recorre clientes o ciudades
            # obtener el nodo de inicio "k" y el nodo destino "l" en la ruta i
            cliente_k =  soluciones[i,cliente] #cliente k de la ruta i
            cliente_l =  soluciones[i, cliente+1] #cliente l de la ruta i
            
            # indexa el valor de Tao
            Tao[cliente_k,cliente_l] = Tao[cliente_k,cliente_l] + delta
            
        # actualizar feromona para la ultima ciudad del circuito (requerido ya que el arco de retorno es una abstracción en el vecto de solución)
        cliente_k = soluciones[i,n-1]
        cliente_l = soluciones[i,n]
        Tao[cliente_k,cliente_l] += delta
    
    return Tao