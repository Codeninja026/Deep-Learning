

import cv2
import numpy as np

img = cv2.imread('Img/cat_test.jpg')

cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
