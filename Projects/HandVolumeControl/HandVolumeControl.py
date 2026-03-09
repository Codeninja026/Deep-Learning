
from HandDetect import  HandDetect
import cv2
import time
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import numpy as np



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))



cap = cv2.VideoCapture(0)
prev_time = 0
curr_time = 0

obj = HandDetect()
while True:
    ret, frame = cap.read()

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    frame  = obj.findHands(frame)
    frame,cordinates = obj.point_coordinates(frame)
    if len(cordinates)!=0:
        x1,y1 = cordinates[4][1] ,cordinates[4][2]
        x2,y2 = cordinates[8][1],cordinates[8][2]
        res = math.sqrt((  (x2-x1)**2)  +  ((y2-y1)**2)  )

        cv2.circle(frame,(x1,y1),12,(255,0,0),cv2.FILLED)
        cv2.circle(frame, (x2, y2), 12, (255, 0, 0), cv2.FILLED)

        cv2.line(frame, (x1,y1),(x2,y2),(255,0,0), 3)
        min_dist = 20  # hand closed
        max_dist = 200  # hand open
        volume_percent = np.interp(res, [min_dist, max_dist], [0, 100])
        cv2.putText(frame, f"{int(volume_percent)}%", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,0), 3)
        volume.SetMasterVolumeLevelScalar(volume_percent/ 100.0, None)


    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("window", frame)


    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()