import cv2
import numpy as np
import mediapipe as mp
import time


class HandDetect:
    def __init__(self,mode=False,max_num_hands=2,min_detection_confidence = 0.7,min_tracking_confidence = 0.7):

        self.mode = mode
        self.maxHands = max_num_hands
        self.detection_confidence = min_detection_confidence
        self.track = min_tracking_confidence
        self.mp_hands_p = mp.solutions.hands
        self.mp_hands = self.mp_hands_p.Hands(self.mode,self.maxHands,1,self.detection_confidence,self.track)
        self.draw_ = mp.solutions.drawing_utils

    def findHands(self,img):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.mp_hands.process(img)
        if self.results.multi_hand_landmarks:
            for hands in self.results.multi_hand_landmarks:
               self.draw_.draw_landmarks(img,hands,self.mp_hands_p.HAND_CONNECTIONS)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        return img


    def point_coordinates(self,img,draw_land=True):

        l1 = []
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                for id,lm in enumerate(hand.landmark):
                    h,w,c = img.shape
                    cx = int(lm.x*w)
                    cy = int(lm.y*h)
                    l1.append([id,cx,cy])
                    if draw_land:
                        cv2.circle(img, (cx, cy), 5, (0,0,255), cv2.FILLED)
        return img,l1

def main():
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
            print(cordinates[4])
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("window", frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
