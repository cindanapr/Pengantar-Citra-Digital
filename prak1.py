import numpy as np
import cv2

#load
images = cv2.imread("lucas.jpg")

#cv2.namedWindow("Lucas", cv2.WINDOW_NORMAL)

imgColor = cv2.imread('lucas.jpg',1) #ke rgb 1 rgb,
imgGrayscale = cv2.imread('lucas.jpg', 0) #ke GrayScale
imgUnchanged = cv2.imread('lucas.jpg', -1) #ke biasa
#cv2.imshow("Lucas", imgGrayscale) #yg dipanggil siapaa
cv2.waitKey(0) #Untuk Menampilkan gambar agar tidak tertimpa lagi


k = cv2.waitKey(0) #buat programnya terhenti kalo pencet tombol s
if k == ord('s'):
    cv2.imwrite('lucas.jpg', imgGrayscale) #buat export
    cv2.destroyAllWindows()

#Membaca Pixel
image = cv2.imread('lucas.jpg')
row,col,ch = image.shape #dapetin nilai
print("row="+str(row)+"; col="+str(col))

#Bikin Canvas Baru #buat ngedit di canvas baru jadi gangeubah
treszero = np.zeros((row,col,3), np.uint8)  #3 itu channel rgb

#Akses Pixel
for k in range (0,row):
    for l in range (0,col):
        blue, green, red = image[k,l] #0 1 2 dari titik k,l
        if blue < 100:
            treszero.itemset((k,1,0), blue) #buat dapetin nilai rgb tpi di opencv dibalik jadi bgr
            treszero.itemset((k,l,1), green)
            treszero.itemset((k,l,2), red)

cv2.imshow("COBA", treszero)
cv2.waitKey(0)
