

import cv2
import numpy as np


#alpha = float(input('* Enter the alpha value [1.0-3.0]: '))     # Simple contrast control
#beta = int(input('Enter the beta value [0-100]: '))             # Simple brightness control
alpha = 1.0

print " Basic Linear Transforms "
print "-----------------------------"

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

new_img = cv2.multiply(img,np.array([alpha]))                    # mul_img = img*alpha
new_img = cv2.add(new_img,np.array([100.3]))                      # new_img = img*alpha + beta

cv2.imshow('original_image', img)
cv2.imshow('new_image',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
