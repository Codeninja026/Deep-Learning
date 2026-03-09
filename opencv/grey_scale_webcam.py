
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    grey_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("window",grey_img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()