import cv2
import numpy as np

image = cv2.imread("ilkom.jpg")

#1 Ubah citra asli ilkom.jpg menjadi grayscale

row,col,ch = image.shape #dapetin nilai
print("row="+str(row)+"; col="+str(col))
#Bikin Canvas Baru #buat ngedit di canvas baru jadi gangeubah
treszero = np.zeros((row,col,1), np.uint8)  #3 itu channel rg' #Grayscale cuma 1

#Ubah Pixel
for k in range (0,row):
    for l in range (0,col):
     blue, green, red = image[k,l] #0 1 2 dari titik k,l
     Gray = (red * 0.299 + green * 0.587 + blue * 0.114)
     treszero.itemset((k,l,0), Gray)

cv2.imshow("Ilkom Gray", treszero)
cv2.waitKey(0)

=====================================================
#2 Ubah citra asli ilkom.jpg menjadi invertnya
import numpy as np
import cv2

image = cv2.imread("ilkom.jpg")

row,col,ch = image.shape #dapetin nilai
print("row="+str(row)+"; col="+str(col))

invert = np.zeros((row,col,3), np.uint8) #channel rgb3

for k in range (0,row):
    for l in range (0,col):
     blue, green, red = image[k,l] #0 1 2 dari titik k,l
     invert.itemset((k,l,0), 255-blue) #buat dapetin nilai rgb tpi di opencv dibalik jadi bgr
     invert.itemset((k,l,1), 255-green)
     invert.itemset((k,l,2), 255-red)

cv2.imshow("Ilkom", image)
cv2.imshow("Ilkom Invert", invert)
cv2.waitKey(0)

#========================================
#3. Dari citra grayscale yang dihasilkan, lakukan tresholding tozero dengan treshold 150
import cv2
import numpy as np
image = cv2.imread("ilkom.jpg")

row,col,ch = image.shape #dapetin nilai
print("row="+str(row)+"; col="+str(col))

treshold = np.zeros((row,col,1), np.uint8)

for k in range (0,row):
    for l in range (0,col):
     blue, green, red = image[k,l] #0 1 2 dari titik k,l
     Gray = (red * 0.299 + green * 0.587 + blue * 0.114)
     Tres = Gray # kalo misalnya tresholdnya 150, tetap dimasukkan nilai yang gray
     if (Tres <= 150): # Threshold ToZero, kalo kecil dari
         Tres=0
     treshold.itemset((k,l,0), Tres)

cv2.imshow("Ilkom Threshold", treshold)
cv2.waitKey(0)
