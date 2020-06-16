import cv2
import numpy as np

def nada(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Original")

# Cria-se um trackbar para cada variável que altera o filtro de cor desejada
cv2.createTrackbar("Cor Inferior", "Original", 0, 255, nada)
cv2.createTrackbar("Cor Superior", "Original", 255, 255, nada)
cv2.createTrackbar("Saturação Inferior", "Original", 0, 255, nada)
cv2.createTrackbar("Saturação Superior", "Original", 255, 255, nada)
cv2.createTrackbar("Valor Inferior", "Original", 0, 255, nada)
cv2.createTrackbar("Valor Superior", "Original", 255, 255, nada)

while True:
    # Vincula os trackbars às suas respectivas variáveis
    lower_h = cv2.getTrackbarPos("Cor Inferior", "Original")
    upper_h = cv2.getTrackbarPos("Cor Superior", "Original")
    lower_s = cv2.getTrackbarPos("Saturação Inferior", "Original")
    upper_s = cv2.getTrackbarPos("Saturação Superior", "Original")
    lower_v = cv2.getTrackbarPos("Valor Inferior", "Original")
    upper_v = cv2.getTrackbarPos("Valor Superior", "Original")
    
    _, frame = cap.read()

    # Converte a leitura BGR para a leitura HSV (Hue, Saturation, Value)
    # Trabalhar com HSV é mais facil pois a cor depende majoritariamente apenas do HUE
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Cria-se um limite inferior e superior contendo os valores obtidos dos trackbars
    limite_inferior = np.array([lower_h, lower_s, lower_v])
    limite_superior = np.array([upper_h, upper_s, upper_v])

    # Essa função retorna uma imagem branca e preta, sendo 0 preto e 255 branco
    # O pixel é 255 se tem os 3 valores (HSV) dentro dos limites estipulados, e é preto se não tiver
    mask = cv2.inRange(hsv, limite_inferior, limite_superior)

    # Por fim, caso o pixel da mask seja branco, este volta a sua cor original
    # Isso é devido à operação and que verifica se ambos valores forem diferente de preto, ela recebe o valor em frame
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Mascara', mask)
    cv2.imshow('Resultado', res)

    if cv2.waitKey(5) == 27:
        break



cap.release()
cv2.destroyAllWindows()
