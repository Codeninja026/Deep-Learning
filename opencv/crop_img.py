
import numpy as np
import cv2

img = cv2.imread("Img/cat_test.jpg")

new_img = img[0:300,0:300]
cv2.imshow("window",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()