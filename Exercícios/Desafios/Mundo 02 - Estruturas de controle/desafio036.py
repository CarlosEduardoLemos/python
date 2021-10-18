casa = float(input('Qual o valor da casa?R$ '))
sal = float(input('Qual o seu salário?R$ '))
ano = int(input('Quantos anos pretende pagar a casa? '))
prestação = casa / (ano * 12)
minimo = sal * 30/100
print('Para pagar a casa de R${:.2f} em {} anos'.format(casa, ano), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if minimo <= sal:
    print('Empréstimo Aprovado')
else:
    print('Empréstimo Negado')
