###   UTILIZANDO MÓDULOS ---> COMANDO 'IMPORT'

###   import bebida  ====>  importa todos os tipos de bebida
###   import doces   ====>  importa todos os tipos de doces

###   from bebida import suco   ====>   importa uma bebida específica
###   from doce import pudim    ====>   importa um doce específico

###   no caso 'bebidas' e 'doces' são bibliotecas quando se fala em programação,

###   math ====> biblioteca com funcionalidades extras de matemática. A sintaxe fica:

###   import math

###   ceil    ===>   arredondamento para cima
###   floor   ===>   arredondamento para baixo
###   trunc   ===>   truncar números, eliminar números a partir da vírgula sem arredondamento
###   pow     ===>   potência   (funciona de forma semelhante aos **)
###   sqrt    ===>   raiz quadrada (square root)
###   factorial   ===>   

###   usar o comando 'from' faz com que importe apenas uma funcionalidade específica, a fim de economizar memória. 
###   A sintaxe fica:

###   from math import sqrt

###   PRÁTICA   ###

import math       ###   caso haja importação de apenas uma funcionalidade ou mais de uma específica a sintaxe fica:   from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = math.sqrt(num)              ###  A sintaxe também pode ser substituída   ===>   raiz = sqrt(num)   ===>   caso apenas a biblioteca específica seja importada

print('A raiz de {} é igual a {}'.format(num, raiz)) ### caso apenas uma ou duas funcionalidades forem importadas, a sintaxe fica:  ===>  .format(num, floor(raiz))

###   para exibir o resultado arredondando para mais é possível escrever  ===>  .format(num, math.ceil(raiz))
###   outra forma de formatar a raiz com duas casas decimais é utilizar   ===>  {:.2f}

### import random
### num = random.random()                ====>   biblioteca para gerar números aleatórios
### print(num)                           ====>   exibe um número aleatório entre 0 e 1

### num = random.randint(1, 10)          ====>   para randomizar um número inteiro de 1 até 10

### docs   ===>   documentação da versão python
### Pypi   ===>   packet index  =  índice de pacotes extras do Python    =   índice de módulos/bibliotecas que podem ser importadas para sua IDE

# import emoji

# print(emoji.emojize('Olá mundo :sunglasses: ', language='alias'))    ### na aula a sintaxe após a frase string é:  , use_aliases=True)) ===> provavel atualização da biblioteca