dista = float(input('Qual a distância da sua viagem? '))
if dista <= 200:
    valor = dista * 0.50
    print('O valor da viagem é {:.2f} reais'.format(valor))
else:
    valor = dista * 0.45
    print('O valor da viagem é de {:.2f} reais'.format(valor))
