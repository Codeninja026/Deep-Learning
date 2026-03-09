
import cv2
import numpy as np

from keras.models import load_model
# from tensorflow.keras.utils import img_to_array

# model_ = load_model('model.h5')
cap = cv2.VideoCapture(0)


while True:
    ret,frame = cap.read()

    cv2.imshow("window",frame)
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

cv2.destroyAllWindows()

# def predict_model(img):
#     img = cv2.resize(img,(244,244))
#     img = img_to_array(img)
#     img  = img / 255.0
#     img = img.reshape(1,244,244,3)
#     return model_.predict(img)


