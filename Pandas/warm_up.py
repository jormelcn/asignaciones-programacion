# Ejercicio de pre-calentamiento


import pandas as pd
import numpy as np

# 1. Cargue en un dataframe el dataset contenido en el archivo CSV /parks.csv Convierta a la columna 'Park Code' en el indice de su dataframe
data = pd.read_csv('./parks.csv', index_col=['Park Code'])


# 2. Visualice las primeras 12 filas del dataframe
print('\nPrimeras 12 filas de los datos:')
print(data.iloc[0:12])

# 3. Visualice las filas 15 a 20 del dataframe
print('\nFilas de la 15 a la 20:')
print(data.iloc[15:21])

# 4. Obtenga el promedio de la columna 'Acres' para las entradas 15 a 20 del dataframe
print('\nPromedio de la columna Acres:')
print(np.mean(data['Acres']))

# 5. Obtenga el nombre del parque indexado por el codigo 'GRSA'
print('\nNombre del parque indexado por el codigo "GRSA":')
print(data.loc['GRSA']['Park Name'])

# 6. Obtenga el total de 'Acres' qie suman los parques con codigos 
print('\nSuma Total de Acres de lo parques con codigos GRSA, YELL y BADL:')
print(np.sum(data.loc[['GRSA', 'YELL', 'BADL']]['Acres']))


# 7. Obtenga el numero de parques cuyo valor en 'Acres' es menor a 10000
print('\nNumero de parques cuyo valor en Acres es menor a 10000:')
print(len(data[data['Acres'] < 10000]))

# 8. Obtenga el numero de parques cuya 'Longitude' es menor a -90
print('\nNumero de parques cuya longitud es menor a -90:')
print(len(data[data['Longitude'] < -90]))

# 9. Obtenga el percentil 75 para la columna 'Acres'
print('\nPercentil 75 para la columba Acres:')
print(data['Acres'].quantile(.75))

# 10. Obtenga las entradas del dataframe cuyos 'Acres' sean mayores al percentil 75 y ordenelos en orden ascendente por 'Acres'
print('\nElementos con Acres mayor al percentil 75 ordenados en forma ascendente:')
print(data[data['Acres'] > data['Acres'].quantile(.75)].sort_values(by='Acres'))

# 11. Obtenga el nombre del parque cuyos 'Acres' son mayores y casi iguales a los del parque Yellowstone National Park
print('\nNombre del Parque cuyos Acres son imediatamente mayores a los del parque Yellowstone:')
yellowstoneAcress = data[data['Park Name'] == 'Yellowstone National Park'].iloc[0]['Acres']
print(data[data['Acres'] > yellowstoneAcress].sort_values(by='Acres').iloc[0]['Park Name'])

# 12. Obtenga el nombre del parque no perteneciente a Alaska que tenga el mayor numero de 'Acres'
print('\nNombre del Parque no perteneciente a alaska que tenga el mayor numero de Acres:')
print(data[data['State'] != 'AK'].sort_values(by = 'Acres').iloc[-1]['Park Name'])


# 13. Obtenga el numero de parques cuyo territorio esta en mas de un estado a la vez
print('\nNumero de Parques cuyo territorio esta en mas de un estado a la vez:')
print(len(data[data['State'].apply(lambda states : len(states.split(',')) > 1)]))

# 14. obtenga el total de 'Acres' de los parques que se encuentran en los estados a los que pertecene el parque Yellowstone National Park
print('\nTotal de Acres de los parques que se encuentran en los estados a los que pertenece el parque Yellowstone:')
yellowstoneStates = data[data['Park Name'] == 'Yellowstone National Park'].iloc[0]['State'].split(',')
print(np.sum(data[data['State'].apply(lambda state : state in yellowstoneStates)]['Acres']))