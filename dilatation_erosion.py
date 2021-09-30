#Chargement d'une image N&B
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('img/smiley.png',0)
#plt.imshow(image, cmap='gray')
#plt.show()

kernel_cross = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
print(kernel_cross)
#plt.imshow(kernel_cross,cmap='gray')
#plt.show()
#cv.imshow("Kernel cross", kernel_cross)
#cv.waitKey(0)
#cv.destroyAllWindows()

kernel_circle = cv.getStructuringElement(cv.MORPH_ELLIPSE,(20,20))
print(kernel_circle)
#cv.imshow("Kernel circle", kernel_circle)
#cv.waitKey(0)
#cv.destroyAllWindows()
#plt.figure()
#plt.imshow(kernel_circle,cmap='gray')
#plt.show()

kernel_rect = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
print(kernel_rect)
#plt.figure()
#plt.imshow(kernel_rect,cmap='gray')
#plt.show()
#cv.imshow("Kernel rect", kernel_rect)
#cv.waitKey(0)
#cv.destroyAllWindows()

def convolution (image,filtre,function):
    new_image = np.zeros(image.shape,np.uint8)
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            new_image[i,j] = function(image,i,j,filtre)
    return new_image
    
def pixel_dilatation(image, ligne, colonne, elmt_structurant):
    width = elmt_structurant.shape[0] // 2
    height = elmt_structurant.shape[1] // 2
    pixel_value = False;
    for i in range(0,elmt_structurant.shape[0]):
        for j in range(0,elmt_structurant.shape[1]):
            x_image = ligne + i - width
            y_image = colonne + j - height
            if ((x_image >= 0) and (x_image < image.shape[0]) and
                (y_image>=0) and (y_image<image.shape[1])):
                if(image[x_image,y_image] and elmt_structurant[i,j]):
                    pixel_value = True
    return pixel_value

def dilatation(image, elmt_structurant):

    return convolution(image,elmt_structurant,pixel_dilatation)
    
def pixel_erosion(image, ligne, colonne, elmt_structurant):

    width = elmt_structurant.shape[0] // 2
    height = elmt_structurant.shape[1] // 2
    pixel_value = True;

    for i in range(0,elmt_structurant.shape[0]):
        for j in range(0,elmt_structurant.shape[1]):
            x_image = ligne + i - width
            y_image = colonne + j - height

            if((x_image >= 0) and (x_image < image.shape[0]) and (y_image>=0) and (y_image<image.shape[1])):
                if (elmt_structurant[i,j] and not(image[x_image,y_image])):
                    pixel_value = False

    return pixel_value

def erosion(image, elmt_structurant):

    return convolution(image,elmt_structurant,pixel_erosion)

kernel_cross = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
cv.imwrite("img/smiley_dilatation.png", dilatation(image,kernel_cross))
cv.imwrite("img/smiley_erosion.png", erosion(image,kernel_cross))