# Matrices de distancias entre nodos para las 3 instancias del problema

#Instancia 1 TSP: 5 nodos"
distances1=[
  [0,8,4,9,9],
  [8,0,6,7,10],
  [4,6,0,5,6],
  [9,7,5,0,4],
  [9,10,6,4,0]]

#Instancia 2 TSP: 7 nodos
distances2=[
  [0,12,8,29,18,25,22],
  [12,0,14,40,30,26,10],
  [8,14,0,27,21,17,23],
  [29,40,27,0,18,32,50],
  [18,30,21,18,0,35,40],
  [25,26,17,32,35,0,30],
  [22,10,23,50,40,30,0]]

#Instancia 3 TSP: 12 nodos
distances3=[
  [0,12,8,29,18,25,22,17,15,32,32,32],
  [12,0,14,40,30,26,10,23,26,40,23,20],
  [8,14,0,27,21,17,23,10,14,26,37,33],
  [29,40,27,0,18,32,50,22,14,14,62,59],
  [18,30,21,18,0,35,40,24,10,29,48,50],
  [25,26,17,32,35,0,30,11,25,23,47,37],
  [22,10,23,50,40,30,0,31,36,48,18,10],
  [17,23,10,22,24,11,31,0,14,17,46,40],
	[15,26,14,14,10,25,36,14,0,20,47,46],
  [32,40,26,14,29,23,48,17,20,0,63,57],
  [32,23,37,62,48,47,18,46,47,63,0,17],
  [32,20,33,59,50,37,10,40,46,57,17,0]]

import numpy as np

#Heuristica Constructiva Insercion del mas cercano
def nearInsertion(distances):
  dist = np.array(distances)
  tour = np.zeros(len(dist), dtype=int)
  notVisited = np.ones(len(tour), dtype=bool)
  notVisited[0] = False
  for i in range(1, len(tour)):
    nearDist = np.min(dist[tour[i-1]][notVisited])
    tour[i] = np.where(np.logical_and(dist[tour[i-1]] == nearDist, notVisited))[0][0]
    notVisited[tour[i]] = False
  return tour

#Calcula la distancia del recorrido
def tourDistance(tour, distances):
  d = [distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1)]
  return sum(d) + distances[tour[-1]][tour[0]]

#Heuristica de mejoramiento  2-opt
def twoOptimice(tour, distances):
  change = True
  while change:
    change = False
    for i in range(len(tour)):
      for j in range(len(tour)):
        if i == j : continue
        swap = np.copy(tour)
        swap[i], swap[j] = swap[j], swap[i]
        if tourDistance(swap, distances) < tourDistance(tour, distances):
          tour = swap
          change = True
  return tour

#Solucionar TSP 
tour1 = nearInsertion(distances1)
optTour1 = twoOptimice(tour1, distances1)

tour2 = nearInsertion(distances2)
optTour2 = twoOptimice(tour2, distances2)

tour3 = nearInsertion(distances3)
optTour3 = twoOptimice(tour3, distances3)

print('Solucion 1: ', optTour1)
print('Solucion 2: ', optTour2)
print('Solucion 3: ', optTour3)

