import numpy as np
import cv2

img = cv2.imread("Img/cat_test.jpg")

# rectangle
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)
#circle
cv2.circle(img,center=(300,300),radius=50,color=(0,255,0),thickness=3)

cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



