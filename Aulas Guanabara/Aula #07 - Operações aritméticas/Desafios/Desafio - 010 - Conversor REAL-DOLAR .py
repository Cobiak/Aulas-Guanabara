###   CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR (CONSIDERAR O DOLAR A R$ 3,27)

real = float(input('Quanto dinheiro você tem na carteira? '))

dolar = real / 3.27

print('Você possui um valor de US$ {:.2f} dólares.'.format (dolar))