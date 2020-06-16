import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(5,5),0)

    _,otsu_b = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    edges = cv2.Canny(otsu_b, 100, 200)
   
    cv2.imshow('Original', frame)
    cv2.imshow('Arestas', edges)
    # cv2.imshow('Sem blur', otsu)
    # cv2.imshow('Com blur', otsu_b)

    if cv2.waitKey(5) == 27:
        break



cap.release()
cv2.destroyAllWindows()
