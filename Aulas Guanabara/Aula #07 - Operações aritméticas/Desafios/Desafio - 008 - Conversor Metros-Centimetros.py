###   ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS


met = int(input('Digite um valor em metros para converter: '))

cent = met * 100
mili = met * 1000

print(' O valor de {} metros é equivalente a {} centímetros e {} milímetros'.format(met, cent, mili))