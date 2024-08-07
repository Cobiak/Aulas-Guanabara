###   FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SEU SUCESSOR E SEU ANTECESSOR   ###

n1 = int(input('Digite um número: '))
suc = n1 + 1
ant = n1 - 1

print('O número {} tem como seu antecessor o número {} e seu sucessor o número {}'.format(n1, ant, suc))