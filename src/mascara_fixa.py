import cv2
import numpy as np

img1 = cv2.imread('../imagens/imagem1.jpeg')
img2 = cv2.imread('../imagens/imagem2.jpeg')

#linhas, colunas, cores = img1.shape # Da o valor máximo de linhas e colunas 

#roi = img1[0:linhas, 0:colunas] # Pega os vetores BGR de todos os pixels da imagem 1
#roi2 = img2[0:linhas, 0:colunas] # Pega os vetores BGR de todos os picels da imagem 2

# converte a img1 na escala cinza
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 

# Tudo que for acima da intensidade de 100 passa a ser branco, e abaixo preto.
ret, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) 

# Tudo que era branco passa a ser preto, e vice versa
mask_inv = cv2.bitwise_not(mask) 

# Cria uma imagem res, onde os pixels brancos da mask passam a ser o pixels da img1, e o resto é preto
res = cv2.bitwise_and(img1, img1, mask=mask_inv) 

# Cria uma imagem res2, onde os pixels brancos da mask_inv passam a ser o pixels da img2, e o resto é preto
res2 = cv2.bitwise_and(img2, img2, mask=mask) 

#Soma o valor dos pixels do resultado 1 com resultado 2, ou seja, onde em uma imagem é preto, passar a ser o pixel da outra imagem
final = cv2.add(res, res2) 

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
cv2.imshow('final', final)   
# cv2.imshow('mask', mask)

cv2.waitKey(0)    
cv2.destroyAllWindows()
