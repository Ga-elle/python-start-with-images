import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("img/Lena_with_message_to_hide.png")
image2 = cv.imread("img/Lena_with_hidden_message.png")


# Extrait le contenu caché en bit de poids faible de la composante B
b,v,r = cv.split(image2)         # récupère 3 matrices d'octets séparées
#image:
cache = b & 1                   # extrait le 1er bit (de poids faible)
#image2:
cache = (b & 1)^(v & 1)  # extrait le 1er bit de B modulé par le 1er bit de V
cache = cache * 255             # multiplie par 255 pour visualiser du noir ou du blanc

cv.imshow("Contenu caché", cache)
cv.waitKey(0)
cv.destroyAllWindows()