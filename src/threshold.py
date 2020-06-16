import cv2
import numpy as np

# Função que é chamada toda vez que o valor do threshold muda.
def nada(x):
    pass

img = cv2.imread('../imagens/kvothe.jpg', cv2.IMREAD_GRAYSCALE)

blur = cv2.GaussianBlur(img,(5,5),0)

# Cria uma janela chamada Original, que será a mesma onde ficará a imagem original.
cv2.namedWindow("Original")

# Cria um trackbar chamado Threshold, na janela original, com valor incial em 0 e com máximo em 255. 
# O valor que o trackbar se incializa é 128.
# Chama a função nada toda vez que esse valor é alterado.
cv2.createTrackbar("Threshold", "Original", 128, 255, nada)

while True:

    # Atualiza a variável 'valor' com o valor atual do trackbar
    valor = cv2.getTrackbarPos("Threshold", "Original")

    # Valores abaixo de 'valor' tornam-se pretos, e os acima tornam-se brancos
    _,binary = cv2.threshold(img, valor, 255, cv2.THRESH_BINARY)

    # Valores abaixo de 'valor' tornam-se brancos, e os acima tornam-se pretos
    _,binary_inv = cv2.threshold(img, valor, 255, cv2.THRESH_BINARY_INV)

    # Valores abaixo de 'valor' sao mantidos iguais, e os acima são convertidos para 'valor'
    _,trunc = cv2.threshold(img, valor, 255, cv2.THRESH_TRUNC)

    # Valores abaixo de 'valor' tornam-se pretos, e os acima são mantidos iguais
    _,tozero = cv2.threshold(img, valor, 255, cv2.THRESH_TOZERO)

    # Valores abaixo de 'valor' são mantidos iguais, e os acima tornam-se pretos 
    _,tozero_inv = cv2.threshold(img, valor, 255, cv2.THRESH_TOZERO_INV)

    # Aqui nao importa o valor, pois ele é determinado automaticamente com base na imagem
    # Otsu é o melhor filtro para imagens proximas de binario, com cores bem contrastantes
    _,otsu = cv2.threshold(blur, valor, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    cv2.imshow('Original', img)
    cv2.imshow('binary', binary)
    cv2.imshow('binary_inv',binary_inv)
    cv2.imshow('trunc', trunc)
    cv2.imshow('tozero', tozero)
    cv2.imshow('tozero_inv', tozero_inv)
    cv2.imshow('otsu', otsu)


    # O valor '50' é o tempo a se esperar até que algum botão seja pressionado
    # Dessa forma, as imagens são atualizadas a cada 50ms.
    key = cv2.waitKey(50)
    if key == 27:
        break

  
cv2.destroyAllWindows()
