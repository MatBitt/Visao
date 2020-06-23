import cv2
import numpy as np

cap = cv2.VideoCapture(0)

motion = cv2.createBackgroundSubtractorMOG2()

while True:
    _, frame = cap.read()

    mask = motion.apply(frame)

    acao = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Original', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('acao', acao)




    if cv2.waitKey(50) == 27:
        break


cap.release()
cv2.destroyAllWindows()
