import cv2
import numpy as np

# Função que é chamada toda vez que o valor do threshold muda.
def nada(x):
    pass

img = cv2.imread('../imagens/kvothe.jpg', cv2.IMREAD_GRAYSCALE)

# Cria uma janela chamada Original, que será a mesma onde ficará a imagem original.
cv2.namedWindow("Original")

# Cria um trackbar chamado Threshold, na janela original, com valor incial em 0 e com máximo em 255. 
# O valor que o trackbar se incializa é 128.
# Chama a função nada toda vez que esse valor é alterado.
cv2.createTrackbar("C", "Original", 1, 10, nada)

cv2.createTrackbar("Tamanho", "Original", 5, 60, nada)

while True:

    # Atualiza a variável 'valor' com o valor atual do trackbar
    c = cv2.getTrackbarPos("C", "Original")

    blockSize = cv2.getTrackbarPos("Tamanho", "Original")

    if blockSize == 0:
        blockSize = 1

    # Valores abaixo de 'valor' tornam-se pretos, e os acima tornam-se brancos
    mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 2*blockSize+1, c)

    # Valores abaixo de 'valor' tornam-se brancos, e os acima tornam-se pretos
    gaus = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 2*blockSize+1, c)

    cv2.imshow('Original', img)
    cv2.imshow('mean', mean)
    cv2.imshow('gaus', gaus)


    # O valor '50' é o tempo a se esperar até que algum botão seja pressionado
    # Dessa forma, as imagens são atualizadas a cada 50ms.
    key = cv2.waitKey(50)
    if key == 27:
        break

  
cv2.destroyAllWindows()
