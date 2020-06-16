import cv2
import numpy as np

# Função que é chamada toda vez que o valor do threshold muda.
def nada(x):
    pass

# Vincula a camêra em '0' com a variável cap
cap = cv2.VideoCapture(0)

# Cria uma janela chamada Original, que será a mesma onde ficará a imagem original.
cv2.namedWindow("Original")

# Cria um trackbar chamado Tamanho, na janela original, com valor incial em 0 e com máximo em 2. 
# O valor que o trackbar se incializa é 0.
# Chama a função nada toda vez que esse valor é alterado.
cv2.createTrackbar("Tamanho", "Original", 0, 2, nada)

while True:

    # Lê o frame atual da câmera
    _, frame = cap.read()

    # Atualiza a variável 'tamanho' com o valor atual do trackbar
    tamanho = cv2.getTrackbarPos("Tamanho", "Original")

    # Converte a frame na escala cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Essa função usa uma imagem, um tipo de variavel e um tamanho de 'filtro' a ser aplicado que deve ser ímpar
    # Usa gradiente para tentar reconhecer bordas
    Laplace = cv2.Laplacian(gray, cv2.CV_64F, ksize=tamanho*2+1)

    # Apos usarmos cv2.CV_64F é utilizado um float de 64 bits para a operação cv2.Laplacian
    # A função abaixo transofrma os valores em valores sem sinais e converte em 8 bits
    # Desse modo, a gente consegue obter uma acuracidade maior, deixando a imagem mais detalhada
    Laplace_uint = np.uint8(np.absolute(Laplace))

    # Sobel recebe a imagem, o tipo da variavel, duas variaveis booleanas e o tamanho do 'filtro'
    # A primeira variavel booleana indica se a operação sera feita no eixo X. 1 - sim, 2 - nao
    # O mesmo vale para a segunda variavel no eixo Y
    # Ambas nao podem ser simultaneamente 1 ou 0 
    sobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=tamanho*2+1)
    sobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=tamanho*2+1)

    # Aqui converte essas variaveis para um inteiro de 8 bits sem sinal
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))

    # Por fim, se une os bits achados na direcao X com os bits achados na direcao Y
    sobel_uint = cv2.bitwise_or(sobelX, sobelY)

    # Canny recebe a imagem e a margem inferior e superior do threshold
    # Essa função usa gradiente tambem, com um filtro pré determinado de 5x5
    # Após o gradiente, o valor resultante é comparado às margens
    # Se for acima da margem superior é considerado, borda. Se for abaixo da inferior é desconsiderado
    # Se for entre, só é considerado borda se estiver diretamente conectado com um pixel borda
    canny = cv2.Canny(gray, 100, 200)
   
    cv2.imshow('Original', frame)
    cv2.imshow('Laplace', Laplace_uint)
    cv2.imshow('Sobel', sobel_uint)
    cv2.imshow('Canny', canny)

    # O valor '50' é o tempo a se esperar até que algum botão seja pressionado
    # Dessa forma, as imagens são atualizadas a cada 50ms.
    if cv2.waitKey(50) == 27:
        break

cap.release()
cv2.destroyAllWindows()
