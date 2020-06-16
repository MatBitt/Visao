import cv2
import numpy as np

def nada(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Original")

cv2.createTrackbar("Cor Inferior", "Original", 0, 255, nada)
cv2.createTrackbar("Cor Superior", "Original", 255, 255, nada)

cv2.createTrackbar("Saturação Inferior", "Original", 0, 255, nada)
cv2.createTrackbar("Saturação Superior", "Original", 255, 255, nada)

cv2.createTrackbar("Valor Inferior", "Original", 0, 255, nada)
cv2.createTrackbar("Valor Superior", "Original", 255, 255, nada)

while True:
    lower_h = cv2.getTrackbarPos("Cor Inferior", "Original")
    upper_h = cv2.getTrackbarPos("Cor Superior", "Original")

    lower_s = cv2.getTrackbarPos("Saturação Inferior", "Original")
    upper_s = cv2.getTrackbarPos("Saturação Superior", "Original")

    lower_v = cv2.getTrackbarPos("Valor Inferior", "Original")
    upper_v = cv2.getTrackbarPos("Valor Superior", "Original")

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    limite_inferior = np.array([lower_h, lower_s, lower_v])
    limite_superior = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, limite_inferior, limite_superior)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Mascara', mask)
    cv2.imshow('Resultado', res)

    if cv2.waitKey(5) == 27:
        break



cap.release()
cv2.destroyAllWindows()
