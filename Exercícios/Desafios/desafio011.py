larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print('A dimensao da sua parede é {}x{} e sua área é de {}m²'.format(larg, alt, area))
print('A quantidade de tinta que vai ser usada é de {} litros'.format(tinta))
