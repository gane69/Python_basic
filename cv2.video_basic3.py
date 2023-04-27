import cv2

cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    # Ako nema vise frejma
    if not ret:
        break
    
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()