import numpy as np
from scipy.optimize import minimize

def demanda(precio, t, A, B, D):
    return (1/B)*(A - precio * (D + t)/D)


def ingreso(demanda, precio):
    return np.sum(demanda*precio)


t = np.arange(8, 20)
A, B, D = 200, 10, 10

def objetivo(X):
    precio = X[0]
    return 0-ingreso(demanda(precio, t, A, B, D), precio)

def precioPositivo(X):
    precio = X[0]
    return precio

resultado = minimize(objetivo, [450000], method='SLSQP', constraints=[{'type':'ineq', 'fun':precioPositivo}])

if resultado['success'] :
    print('Se encontro el precio ideal: ', resultado['x'][0])
else :
    print('No se encontro un resultado optimo ')
    
