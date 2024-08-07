###    CRIE UM ALGORITMO QUE LEIA UM NÚMERO, MOSTRE SEU DOBRO, MOSTRE SEU TRIPLO E RAIZ QUADRADA.   ###

n1 = int(input('Digite um número: '))

dob = n1 * 2
tri = n1 * 3
rai = n1 ** (1/2)                       ###   ---> por conta da ordem de precedencia inserir parenteses para resolver primeiro o que está entre eles

print('O dobro do número {} é igual a {}, seu triplo é igual a {} e sua raiz é igual a {:.2f}'.format(n1, dob, tri, rai))

### outra forma para realizar os cálculos sem discriminar todas as variáveis é inserir as expressões dentro dos parenteses do comando   .format()
### outra forma de calcular a raiz quadrada é utilizando a função 'pow' (power), nesse caso seria:   pow(n, (1/2))