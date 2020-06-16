import cv2
import numpy as np

# Função que é chamada toda vez que o valor do threshold muda.
def nada(x):
    pass

# Carrega a imagem em tons de cinza
img = cv2.imread('../imagens/kvothe.jpg', cv2.IMREAD_GRAYSCALE)

# Cria uma janela chamada Original, que será a mesma onde ficará a imagem original.
cv2.namedWindow("Original")

# Cria um trackbar chamado C, na janela original, com valor incial em 0 e com máximo em 10. 
# O valor que o trackbar se incializa é 1.
# Chama a função nada toda vez que esse valor é alterado.
cv2.createTrackbar("C", "Original", 1, 10, nada)

cv2.createTrackbar("Tamanho", "Original", 5, 60, nada)

while True:

    # Atualiza a variável 'valor' com o valor atual do trackbar
    c = cv2.getTrackbarPos("C", "Original")

    blockSize = cv2.getTrackbarPos("Tamanho", "Original")

    # Isso é só para impedir que o blocksize seja 1, pois o mínimo é 3 e deve ser sempre ímpar
    if blockSize == 0:
        blockSize = 1

    # Valores abaixo de 'valor' tornam-se pretos, e os acima tornam-se brancos
    # Neste caso, o valor do pixel é uma média dos valores dos pixels considerados no tamanho do bloco
    mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 2*blockSize+1, c)

    # Valores abaixo de 'valor' tornam-se brancos, e os acima tornam-se pretos
    # Neste caso, o valor do pixel é uma média ponderada dos valores dos pixels considerados no tamanho do bloco
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
