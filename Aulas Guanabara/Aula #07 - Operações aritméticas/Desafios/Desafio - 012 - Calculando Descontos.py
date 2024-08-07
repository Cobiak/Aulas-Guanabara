###   FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO


vp = float(input('Qual o valor do produto que você quer comprar? R$ '))
desc = int(input('Qual o valor do desconto que voce gostaria? (em %) '))

vcd = vp - (vp * desc / 100)

print('O produto com o valor de {} com um desconto de {}%, ficará com o valor de R${:.2f}'.format(vp, desc, vcd))