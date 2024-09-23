import os
import pandas as pd
import numpy as np


def cargar_datos() -> np.ndarray: # El np.ndarray es una forma de control
    # load the data from the csv file
    # build the path in in data/A-n33-k6.csv
    path_file = os.path.join('TSP', 'ACO', 'data', 'A-n33-k6.csv')
    
    # read the csv file as numpy array without index
    
    df = pd.read_csv(path_file, header=None)

    # seleccionar columnas de interes
    instance = df.iloc[:,1:3]
    
    # convertir en un array the numpy de tamaño nXm
    coordenadas = instance.to_numpy()
    
    return coordenadas