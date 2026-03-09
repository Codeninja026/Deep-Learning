
import cv2
import numpy as np
from keras.models import load_model
from tensorflow.keras.utils import img_to_array


def predict_model(img):
    img = img_to_array(img)
    img  = img / 255.0
    img = img.reshape(1,244,244,3)
    return model_.predict(img)

model_ = load_model('model.h5')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, (244, 244))
    prediction = predict_model(img)
    if prediction < 0.15:
        label = "mask"
        color = (0,255,0)
    else:
        label = "no mask"
        color = (0,0,255)

    cv2.putText(frame,label,(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
    cv2.imshow("window",frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()



