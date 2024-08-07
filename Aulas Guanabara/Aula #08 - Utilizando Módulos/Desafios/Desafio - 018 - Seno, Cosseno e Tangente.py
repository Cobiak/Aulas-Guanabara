### FAÇA UM PRROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO

import math   #   CASO IMPORTE APENAS FUNCOES ESPECÍFICAS   ===>  from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(ang))       ###   CASO IMPORTE AS FUNÇÕES ESPECÍFICAS, NÃO É PRECISO INSERIR 'MATH' NAS VARIAVEIS
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('O Ângulo de {:.0f}º tem como seu valor em:\n Seno = {:.2f}\n Cosseno = {:.2f} \n Tangente = {:.2f}'.format(ang, seno, cosseno, tangente))