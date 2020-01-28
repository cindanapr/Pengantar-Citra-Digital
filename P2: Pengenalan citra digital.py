import cv2
import numpy as np

image = cv2.imread("sehun.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert color, parameter 1:gambar, 2: ubah warna


cv2.imshow("Sehun", image)
cv2.imshow("Sehun Gray", gray)

cv2.waitKey(0)

#===================================================================================================
#formula yang digunakan untuk mengubah dari RGB ke Grayscale
#Gray = (red * 0.299 + green * 0.587 + blue * 0.114)

row,col,ch = image.shape
canvas_grayscale = np.zeros((row,col,1), np.uint8) #buat bikin  dimensi gambar

#lossless: ada yang hilang sedikit kualitasnya, karna hilang ngambil pixel

