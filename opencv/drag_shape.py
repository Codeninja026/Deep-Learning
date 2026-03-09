
import cv2
import numpy as np

img = np.zeros((500,500,3))

flag=False
ix =-1
iy = -1
def draw(event,x,y,flags,params):
    global flag,ix,iy
    if event==1:
        ix = x
        iy = y
        flag = True
    elif event==0:
        if flag==True:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=-1)
    else:
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=-1)
        flag = False

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)

while True:
    cv2.imshow("window",img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()