print("hello")
#import cv2 as cv
import cv2
print (cv2.__version__)
import numpy as np
print (np.__version__)


#import cv2
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(0)
print(cap)
print(cap2)
while True:

    ret, frame = cap.read()
    frame = cv2.resize(frame,(600,400))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
