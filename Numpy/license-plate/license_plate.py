import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pyl

#Funcion para realizar suma deslizante
def slidingWindowSum(a, w, h):
  fs = np.zeros((a.shape[0], a.shape[1] - w))
  for i in range(fs.shape[0]):
    fs[i,0] = np.sum(a[i,0:w+1])
    for j in range(1, fs.shape[1]):
      fs[i,j] = fs[i, j-1] - a[i, j-1] + a[i, j+w]
  ss = np.zeros((fs.shape[0] - h, fs.shape[1]))
  for j in range(ss.shape[1]):
    ss[0,j] = np.sum(fs[0:h+1,j])
    for i in range(1, ss.shape[0]):
      ss[i,j] = ss[i-1, j] - fs[i-1, j] + fs[i+h, j]
  return ss

#Funcion para realizar ventaneo deslizante concentrico
def slidingConcentricWindows(img, A, B):
  R, R2 = int((B-A)/2), int(B/2)
  MA = slidingWindowSum(img, A, A)[R:-R,R:-R]
  MB = slidingWindowSum(img, B, B)
  return ( ((A+1)**2/(B+1)**2) * (MB/MA), img[R2:-R2,R2:-R2] )

#Cargar imagen
image_color = pyl.imread('./lp3.jpg')

#Convertir a grises
image = np.linalg.norm(image_color, axis=2)
plt.figure()
plt.imshow(image, cmap='gray')

#Aplicando ventanas deslizantes
(scw, image) = slidingConcentricWindows(image, 2, 8)
scw = scw  <= 0.8
#Mostrar imagen resultado de scw
plt.figure()
plt.imshow(255*scw, cmap='gray')

#Determinando lineas verticales y horizontales
hlines = np.sum(scw, axis=1) > 35
vlines = np.sum(scw, axis=0) > 10
#Mostrar lineas horizontales y verticales
roi = np.zeros(scw.shape)
roi[hlines,:] = 255
roi[:,vlines] = 255
plt.figure()
plt.imshow(roi, cmap='gray')

#Derterminar region de interes vertical
hindex = np.arange(0,scw.shape[0])[hlines]
hpivot = np.zeros((len(hindex), len(hindex))) + hindex
hdiff = hpivot - hpivot.T
vzones = np.logical_and(hdiff > 60, hdiff < 70).nonzero()
h_pars = np.vstack((hindex[vzones[0]], hindex[vzones[1]])) 
h_i = np.argmax(h_pars[1,:] - h_pars[0,:])
#Determinar region de interes horizontal
vindex = np.arange(0, scw.shape[1])[vlines]
vpivot = np.zeros((len(vindex), len(vindex))) + vindex
vdiff = vpivot - vpivot.T
hzones = np.logical_and(vdiff > 130, vdiff < 145).nonzero()
v_pars = np.vstack((vindex[hzones[0]], vindex[hzones[1]]))
v_i = np.argmax(v_pars[1,:] - v_pars[0,:])

#Construir mascara para la segmentacion
mask = np.zeros(scw.shape)
mask[h_pars[0,h_i] : h_pars[1,h_i], v_pars[0,v_i] : v_pars[1,v_i]] = 1
#Mostrar segmentacion
plt.figure()
plt.imshow(mask*image, cmap='gray')

#
plt.show()