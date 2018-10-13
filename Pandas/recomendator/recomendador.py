# Sistema de recomendaciones basico usando Pandas 

# La idea de este ejercicio practico es desarrollar un corto script que permite hacer una recomendacion de acuerdo a
# la calificacion y a la popularidad de una pelicula.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#En primer lugar cargue los datasets "ratings.csv" y "movies.csv" en dataframes
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

#Observe los dataframe, que columnas contienen, que datos son relevantes, hay alguna columna en comun entre ambos dataframe

#La recomendacion es de acuerdo a la popularidad y calificacion de las peliculas, sin embargo la calificacion y el nombre
#de la pelicula estan en dataframes distintos, entonces es necesario que combine los dataframe en uno solo, se puede 
#al aprovechar la existencia de una columna en comun (pista: merge)
data = movies.merge(ratings, left_on='movieId', right_on='movieId', how='outer')

#Es comun encontrar peliculas con altas calificaciones ('ratings'), pero no es prenda de garantia de que la pelicula sea
#popular, puede observarse que una pelicula con calificacion de 5 hecha por un solo usuario tiene or tanto una calificacion promedio de 5
#Obtenga y visualice la calificacion (rating) promedio de las peliculas del dataframe, agrupelas por titulo y organice los promedios
#en orden descendente
ratings_values = data.groupby('movieId')['rating'].mean().sort_values(ascending=False)

#Para medir la popularidad de una pelicula es necesario saber cuantos usuarios la han calificado, las peliculas mas populares son por lo general
#las que reciben mas calificaciones de parte de los usuarios. Agrupe las peliculas por titulo y obtenga en orden descendente el numero de calificaciones
#para cada pelicula del dataframe
ratings_count = data.groupby('movieId')['rating'].size().sort_values(ascending=False)

#Ahora implemente un nuevo dataframe cuyas columnas sean la calificacion promedio de la pelicula 'promedio_rating' y la cantidad de calificaciones 'numero_califs'
#que recibio la pelicula. Utilice las operaciones que ya utilizo para medir esas mismos parametros
ratings_info = pd.concat([ratings_values, ratings_count], axis=1)
ratings_info.columns = ['score', 'count']

#Compruebe que estdisticamente las peliculas con mas calificaciones son tambien las peliculas con las mas altas calificaciones en promedio
#Tenga en mente una de las peliculas que se obtengan en este punto, preferiblemente la primera de la lista, con base en esta pelicula se va hacer
#la recomendacion (titulo de la pelicula)
ratings_counts_scores = ratings_info.groupby('count')['score'].mean()
ratings_counts_count = ratings_info.groupby('count')['count'].size()

ratings_counts_dist = ratings_counts_count.multiply(ratings_counts_count.index).sort_index(axis=0, ascending=False)/len(data)
counts_dist_integral = ratings_counts_dist.cumsum()
counts_relevant = counts_dist_integral[counts_dist_integral <= 0.33].index[-1]

relevant_movies = ratings_info[ratings_info['count'] >= counts_relevant].sort_values(by='score', ascending=False)
print(relevant_movies)

#Implemente un nuevo dataframe donde el indice sea la columna 'userID' del dataframe, las columnas sean los titulos de las peliculas y los valores
#sean las calificaciones individuales de cada usuario a las peliculas (pista: pivot)

#Obtenga una lista con las calificaciones que los usuarios dieron a la pelicula mas popular (la que se tiene en mente luego de la comprobacion estadistica)

#Haga una nueva lista con la correlacion entre la lista anterior y el ultimo dataframe que se implemento, en esta instancia se va calcular la correlacion entre 
#todas las peliculas del dataframe y la pelicula mas popular y mejor calificada del dataframe (pista: corrwith)

#Implemente un nuevo dataframe con la ultima lista (la de las correlaciones) y a la columna llamela 'Correlaciones'
#Elimine de esta lista todos los valores NaN

#A este ultimo dataframe agreguele la columna del dataframe donde se registraron la cantidad de calificaciones por pelicula ('numero_califs') (pista: join)

#Visualice las recomendaciones como las peliculas con un numero de calificaciones mayores al percentil 60 del numero de calificaciones por pelicula ('numero_califs')
#y ordene el dataframe en orden descendente de la columna 'Correlaciones'

counts_dist_integral.plot()
plt.title('Distribución del numero de calificaciones')
plt.show()