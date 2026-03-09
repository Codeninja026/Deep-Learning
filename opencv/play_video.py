
import cv2
import numpy as np
import time
cap = cv2.VideoCapture('output.avi')

while True:
    ret ,frame = cap.read()
    time.sleep(1/20)
    cv2.imshow("window",frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()