
import cv2
import numpy as np


img = cv2.imread('Img/cat_test.jpg')

flag = False
ix = -1
iy =-1

def crop(event,x,y,flags,params):
    global flag,ix,iy
    if event==1:
        flag=True
        ix = x
        iy = y
    elif event==4:
        flag = False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=1)
        new_img = img[iy:y,ix:x]
        # cv2.imwrite("Cropped_img.jpg",new_img)
        cv2.imshow("new_window",new_img)
        cv2.waitKey(0)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",crop)


while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


cv2.destroyAllWindows()