

import numpy as np
import cv2

img = cv2.imread("Img/cat_test.jpg")

# 0 1 and -1 to flip vertical,horizontal and both respectively
new_img = cv2.flip(img,-1)
cv2.imshow("window",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()