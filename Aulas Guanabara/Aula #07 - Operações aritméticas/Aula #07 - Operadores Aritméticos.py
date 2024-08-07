   ###   OPERADORES ARITMÉTICOS    ###

##  +  ADIÇÃO                **  POTÊNCIA
##  -  SUBTRAÇÃO             //  DIVISÃO INTEIRA         --->            (NÃO ACRESCENTA VÍRGULA MOSTRA APENAS O NÚMERO INTEIRO)
##  *  MULTIPLICAÇÃO          %  RESTO DA DIVISÃO        --->            (MOSTRA O NÚMERO REAL, OU SEJA, EXIBE O NÚMERO APÓS A VÍRGULA)
##  /  DIVISÃO               ==  OPERADOR RELACIONAL DE IGUALDADE  --->  (USADO EM VÁRIAS LINGUAGENS: C, JAVA, PHP entre OUTRAS)

## todo OPERADOR PRECISA DE OPERANDOS ---> UM OPERANDO PODE SER UM NÚMERO, STRING E VARIÁVEIS


   ###   ORDEM DE PRECEDÊNCIA   ###

##  1)  ()                  (PARENTESES)
##  2)  **                  (POTÊNCIAS/EXPONENCIAÇÃO)
##  3)  * , / , // , %      (MULTIPLICAÇÃO, DIVSÃO, DIVISÃO INTEIRA, RESTO DA DIVISÃO)  ---> nesse caso ela resolve na ordem que elas aparecem
##  4)  + , -               (SOMA e SUBTRAÇÃO)

   ### PRÁTICA ##

##  nome = input('Qual é o seu nome? ')
##  print('Prazer em te conhecer {}!' .format(nome))  ## função comum do print ##

   ###   ALINHAMENTOS   ##

## nome = input('Qual é o seu nome? ')
## print('Prazer em te conhecer{:=^20}!'.format(nome))

##   {:20}    --->   o nome vai aparecer em 20 caracteres
##   {:>20}   --->   o nome vai aparecer com alinhamento à direita
##   {:^20}   --->   o nome vai aparecer centralizado entre os 20 caracteres
##   {:=^20}  --->   o nome vai aparecer centralizado entre vários '=' 

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))    ###   em caso de divisão flutuante adicionar à chave {:.3f} para formatar  ###
print('Divisão inteira {} e potência {}'.format(di, e))

### caso queira que todos os resultados apareçam na mesma linha sem quebra, digitar após o parenteses do comando format   , end=' ')
### caso queira que haja quebra de linha no meio do print, adicionar   \n    no local onde quer que haja a quebra