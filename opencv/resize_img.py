
import numpy as np
import cv2

img = cv2.imread("Img/cat_test.jpg")

new_img = cv2.resize(img,(256,256))
cv2.imshow("window",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()