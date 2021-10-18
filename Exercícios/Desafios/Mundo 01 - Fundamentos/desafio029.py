km = float(input('Digite a sua velocidade atual em Km/h: '))
if km > 80:
    print('Você está acima da velocidade permitida. Você foi multado!!!')
    s = (km - 80) * 7.00
    print('O valor da multa é de {:.2f} reais'.format(s))
else:
    print('Você esta na velocidade permitida')
