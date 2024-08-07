###   UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. 
###   FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME ESCOLHIDO

import random   ### EM CASO DE IMPORTAR FUNÇÃO ESPECÍFICA: from random import choice

a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

lista = [a1, a2, a3, a4]      ###====>  listas ficam entre COLCHETES

escolhido = random.choice(lista)

print('O aluno que vai apagar a lousa hoje é: {}'.format(escolhido))