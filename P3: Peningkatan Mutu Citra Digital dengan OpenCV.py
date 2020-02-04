#========Arithmetic Processing====================
#******************************************
#1. Addition

#jika ingin menambah satu gambar saja
import cv2
import numpy as np

image1 = cv2.imread('gambar1.jpg')
image2 = cv2.imread('gambar2.jpg')

addition = cv2.add(image1, 100) #nilai skalarnya terserah berapa

cv2.imshow('Addition Image', addition)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()

#jika ingin menambahkan 2 gambar

import cv2
import numpy as np

image1 = cv2.imread('gambar1.jpg')
image2 = cv2.imread('gambar2.jpg')

addition = cv2.add(image1, image2)

cv2.imshow('Addition Image', addition)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()

#************************************************
#2. Subtraction, mengurangi gambar

#satu gambar
import cv2
import numpy as np

image1 = cv2.imread('gambar1.jpg')
image2 = cv2.imread('gambar2.jpg')

substraction = cv2.subtract(image1, 100)

cv2.imshow('Substraction Image', substraction)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()

#dua gambar
import cv2
import numpy as np

image1 = cv2.imread('gambar1.jpg')
image2 = cv2.imread('gambar2.jpg')

substraction = cv2.subtract(image1, image2)

cv2.imshow('Substraction Image', substraction)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()

#**********************************************
#3. Multiply

#satu gambar
import cv2
import numpy as np

image1 = cv2.imread('gambar1.jpg')
image2 = cv2.imread('gambar2.jpg')

Multiply = cv2.multiply(image1, 2)

cv2.imshow('Multiply Image', Multiply)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()

#*************************************************
#4. Divide
import cv2
import numpy as np

image1 = cv2.imread('gambar1.jpg')
image2 = cv2.imread('gambar2.jpg')

Divide = cv2.divide(image1,2)

cv2.imshow('Divide Image', Divide)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()


