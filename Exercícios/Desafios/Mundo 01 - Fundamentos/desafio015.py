dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pagar = (dia * 60) + (km * 0.15)
print('O valor total é de R${:.2f}'.format(pagar))
