import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Convertit l'image en niveaux de gris Y
image = cv.imread("img/Lena_original.png")
b,v,r = cv.split(image)         # récupère 3 matrices d'octets séparées
y = 0.299*r + 0.587*v + 0.114*b # opération matricielle
y = y.astype(np.uint8)          # convertit les réels en octets
cv.imshow("Luminance Y", y)

# Calcule l'histogramme de l'image
histo = np.zeros(256, int)      # prépare un vecteur de 256 zéros
for i in range(0,image.shape[0]):       # énumère les lignes
    for j in range(0,image.shape[1]):   # énumère les colonnes
        histo[y[i,j]] = histo[y[i,j]] + 1
print(histo)
plt.plot(histo)
plt.show()

# Calcule l'histogramme cumulé hc
hc = np.zeros(256, int)         # prépare un vecteur de 256 zéros
hc[0] = histo[0]
for i in range(1,256):
    hc[i] = histo[i] + hc[i-1]

# Normalise l'histogramme cumulé
nbpixels = y.size
hc = hc / nbpixels * 255
print(hc)
plt.plot(hc)
plt.show()

# Utilise hc comme table de conversion des niveaux de gris
for i in range(0,y.shape[0]):       # énumère les lignes
    for j in range(0,y.shape[1]):   # énumère les colonnes
        y[i,j] = hc[y[i,j]]
cv.imshow("Luminance Y après égalisation", y)
cv.waitKey(0)
cv.destroyAllWindows()