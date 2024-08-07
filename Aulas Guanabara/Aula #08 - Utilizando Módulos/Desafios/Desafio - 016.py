###   CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA
#     EX:   DIGITE UM NÚMERO: 6.127
#           O NÚMERO 6.127 TEM A PARTE INTEIRA 6

import math

n1 = float(input('Digite um número: '))

print('O número inteiro de {}, é igual a {}'.format(n1, int(n1)))

###   SOLUÇÃO 1   ###

##   utilizando o método trunc após importar 'math':   .format(num, math.trunc(num)))

##   utilizando o método trunc após importar apenas a funcionalidade 'trunc' da biblioteca 'math'   ===>   from math import trunc

##   .format(num, trunc(num)))
