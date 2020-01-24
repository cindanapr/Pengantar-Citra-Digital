import numpy as np
import cv2

#load
images = cv2.imread("indomie.jpg")
#cv2.namedWindow("Lucas", cv2.WINDOW_NORMAL)
imgColor = cv2.imread('indomie.jpg',1) #ke rgb 1 rgb,
imgGrayscale = cv2.imread('indomie.jpg', 0) #ke GrayScale
imgUnchanged = cv2.imread('indomie.jpg', -1) #ke biasa
#cv2.imshow("Lucas", imgGrayscale) #yg dipanggil siapaa
cv2.waitKey(0) #Untuk Menampilkan gambar agar tidak tertimpa lagi

k = cv2.waitKey(0) #buat programnya terhenti kalo pencet tombol s
if k == ord('s'):
    cv2.imwrite('indomie.jpg', imgGrayscale) #buat export
    cv2.destroyAllWindows()

# 1. Buatlah program sederhana untuk membuat matrix gambar
# Membaca Pixel
image = cv2.imread('indomie.jpg')
row,col,ch = image.shape #dapetin nilai
print("row="+str(row)+"; col="+str(col))

#Bikin Canvas Baru #buat ngedit di canvas baru jadi gangeubah
treszero = np.zeros((row,col,3), np.uint8)  #3 itu channel rgb

# untuk menampilkan gambar asli
cv2.imshow("Gambar Asli", image)
# untuk menampilkan gambar baru
cv2.imshow("Gambar Baru", treszero)

# 2.Buatlah program pencari nilai pixel (<150) dan mengganti dengan nilai 255
#Akses Pixel
for i in range(0, row):
    for j in range(0, col):
        blue, green, red = image[i,j]
        if (red < 150 & green < 150 & blue < 150):
            blue, green, red = (255, 255, 255)
        treszero.itemset((i,j,0), blue)
        treszero.itemset((i,j,1), green)
        treszero.itemset((i,j,2), red)

cv2.imshow("Pixel 255", treszero)
cv2.waitKey(0)

#3. Buatlah program untuk membalik matrix (transpose)
transpose = np.zeros((col, row, 3), np.uint8)

for m in range(0, row):
    for n in range(0, col):
        blue, green, red = image[m,n]
        transpose.itemset((n, m, 0), blue)
        transpose.itemset((n, m, 1), green)
        transpose.itemset((n, m, 2), red)

cv2.imshow("Hasil Transpose", transpose)
cv2.waitKey(0)

k = cv2.waitKey()
if k == ord('s'):
    cv2.imwrite("pixel.png", treszero)
    cv2.imwrite("transpose.png", transpose)
cv2.waitKey(0)
cv2.destroyAllWindows()

