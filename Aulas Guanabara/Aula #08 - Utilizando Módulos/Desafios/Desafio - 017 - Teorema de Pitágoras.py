### faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retânglo, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA


#   co = float(input('Digite o comprimento do cateto oposto: '))
#   ca = float(input('Digite o comprimento do cateto adjacente: '))
#   hi = (co ** 2 + ca ** 2) ** (1/2)

#   print('Um triângulo retângulo com o cateto oposto no valor de {}, e com cateto adjacente no valor de {}, terá sua hipotenusa com o valor de {:.2f}.'.format(co, ca, hi))


###   SOLUÇÃO COM A BIBLIOTECA 'MATH'   ###

import math    ###   ====>   from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))   

hi = math.hypot(co, ca)

print('A hipotenusa é igual a {:.2f}.')