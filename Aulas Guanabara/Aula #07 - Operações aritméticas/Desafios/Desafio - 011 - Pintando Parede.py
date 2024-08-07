###   FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA. 
###   SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M²

larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))

area = larg * alt

tinta = area / 2

print('Para uma parede com área de {} m² vão ser necessários {} litros de tinta'.format(area, tinta))