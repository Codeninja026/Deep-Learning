
import numpy as np
import cv2

img = cv2.imread('Img/cat_test.jpg')

# def draw(event,x,y,flags,params):
#     if event==0:
#         print("mouse moved")
#     if event==1:
#         print("mouse clicked")
#     if event==4:
#         print("mouse released")

def draw(event,x,y,flags,params):
    if event==1:
        cv2.circle(img,center=(x,y),radius=50,thickness=0,color=(0,255,0))

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF== ord('x'):
        break
cv2.destroyAllWindows()
