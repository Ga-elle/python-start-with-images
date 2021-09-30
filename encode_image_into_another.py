import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Cache un message d'information (en Noir & Blanc) dans une image

image = cv.imread("img/Lena_original.png")
message = cv.imread("img/message_to_hide.png",0)

b,v,r = cv.split(image)        # récupère 3 matrices d'octets séparées
print(b.shape)
print(message[0][:10])
print(b[0][:10])
b = b & 0b11111110             # efface le bit de poids faible des octets de B
print(b[0][:10])
b = b | (message > 0)          # ajoute le bit de de poids faible en fonction du message
#pour complexifier encodage:
#b = b | (message > 0)^(v&1)  # bit de de poids faible fonction du message et de V
print(b[0][:10])

cache = cv.merge((b,v,r))      # reconstruit une image à partir des 3 plans RVB
cv.imwrite("img/Lena_with_message_to_hide.png", cache)

cv.imshow("Image avec contenu caché", cache)
cv.waitKey(0)
cv.destroyAllWindows()