     ## crie um script que leia dois numeros e tente mostrar a soma entre eles

## n1 = input('Digite um número ')
## n2 = input('Digite outro número ')
## s = n1 + n2
## print('A soma vale', s)  
## código não funciona porque?

##  n1 = int(input('Digite um número: '))
##  n2 = int(input('Digite outro número: '))
##  s = n1+n2

     ## tipos primitivos ##

#   int = numeros inteiros >>> 1,2,3,0 (positivo, negativo ou nulo)
#   float = numeros reais/ponto flutuante >>> 4.5 // 0.75 // -15.233 // 7.0
#   booL = valores lógicos/booleanos >>> true // false
#   str = valores caracteres >>> 'olá' // '7,5' // ''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2

##  print('A soma vale' , s)

     ##   print alternativo   ##

##  print('A soma vale {}'.format{s}

##   n1 = input('Digite um valor: ')
##   n2 = int(input('Digite outro valor'))
##   n3 = float(input(")
##   print(type(n1))     --->   class > str
##   print(type(n2))     --->   class > int


print('A soma entre {} e {}, é igual a {}'.format(n1,n2,s))