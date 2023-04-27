import cv2

cap = cv2.VideoCapture("")

ret, frame = cap.read()

cv2.imshow("Image", frame)
cv2.waitKey(0)