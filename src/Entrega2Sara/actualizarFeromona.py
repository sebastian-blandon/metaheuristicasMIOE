import numpy as np


def actualizarFeromona(Tao:np.ndarray,
                       rho:float,
                       soluciones:np.ndarray,
                       longitud_tours:np.ndarray,
                       m:int,
                       n:int
                       ) -> np.ndarray:
    #evaporación feromona (formulación de la tasa de evaporación)
    Tao =  (1-rho) * Tao    
    
    #actualizar feromona para cada hormiga m
    for hormiga in range(m): #recorre circuitos
        delta:float = 1/longitud_tours[hormiga]       #aumento proporcional a la calidad del circuito
        for cliente in range(n-1): #recorre clientes o ciudades
            # obtener el nodo de inicio "k" y el nodo destino "l" del recorrido de la hormiga 
            cliente_k = soluciones[hormiga,cliente] #cliente k de la ruta i
            cliente_l = soluciones[hormiga, cliente+1] #cliente l de la ruta i
            
            # indexa el valor de Tao
            Tao[cliente_k,cliente_l] = Tao[cliente_k,cliente_l] + delta
    #        
    #    # actualizar feromona para la ultima ciudad del circuito (requerido ya que el arco de retorno es una abstracción en el vecto de solución)
        cliente_k = soluciones[hormiga,n-1]
        cliente_l = soluciones[hormiga,n]
        print("")
        Tao[cliente_k,cliente_l] += delta
    
    return Tao