import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Cria-se um filtro de tamanho (x,y) para servir de parametro nas funções a seguir
filtro = np.ones((5,5), np.uint8)

while True:
    _, frame = cap.read()

    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Embassa a imagem para diminuir o ruído
    blur = cv2.GaussianBlur(gray,(5,5), 0)

    # Realiza o threshold OTSU
    _,mask = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Essa é uma operação de remoção de falsos positivos
    # Deixa de reconhecer muita coisa
    # Para cada positivo, ele olha para seus vizinhos com base no tamanho do filtro e analisa se aquilo é de fato positivo
    erosao = cv2.erode(mask, filtro, iterations = 1)
    
    # Essa é uma operação de remoção de falsos negativos
    # Passa a reconhecer muita coisa
    # Para cada negativo, ele olha para seus vizinhos com base no tamanho do filtro e analisa se aquilo é de fato negativo
    dilatacao = cv2.dilate(mask, filtro, iterations = 1)
    
    # Essa é uma operação de remoção de falsos positivos
    # Deixa de reconhecer muita coisa
    # Para cada positivo, ele olha para seus vizinhos com base no tamanho do filtro e analisa se aquilo é de fato positivo
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, filtro)
    
    # Essa é uma operação de remoção de falsos negativos
    # Passa a reconhecer muita coisa
    # Para cada negativo, ele olha para seus vizinhos com base no tamanho do filtro e analisa se aquilo é de fato negativo
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, filtro)

    # cv2.imshow('Mascara', mask)
    cv2.imshow('Erosao', erosao)
    cv2.imshow('Dilatacao', dilatacao)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)

    if cv2.waitKey(5) == 27:
        break


cap.release()
cv2.destroyAllWindows()
