

import cv2
import numpy as np


img = cv2.imread('Img/cat_test.jpg')

# img[:,:,0] = 0
# cv2.imshow("window",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


Img1 = img[:,:,0]
Img2= img[:,:,1]
Img3 = img[:,:,2]
new_img = np.hstack((Img1,Img2,Img3))
cv2.imshow("window",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()