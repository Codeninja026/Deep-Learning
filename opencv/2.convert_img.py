
import numpy as np
import cv2


img = cv2.imread('Img/cat_test.jpg')

img_conv = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("window",img_conv)
cv2.waitKey(0)
cv2.destroyAllWindows()