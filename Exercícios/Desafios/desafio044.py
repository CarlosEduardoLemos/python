valor = float(input('Qual o valor do produto? R$'))
print('''[1] À vista no dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto.
[3] Em até 2x no cartão: preço normal.
[4] 3x ou mais no cartão: 20% de juros.''')
condi = int(input('Código de pagamento:'))
if condi == 1:
    print('À vista no dinheiro/cheque')
    des = valor - (10/100 * valor)
    print('O valor R${:.2f} com desconto é de R${:.2f}'.format(valor, des))
elif condi == 2:
    print('À vista no cartão')
    des = valor - (5/100 * valor)
    print('O valor R${:.2f} com desconto é de {:.2f}'.format(valor, des))
elif condi == 3:
    print('2x no cartão')
    nvalor = valor / 2
    print('O valor é de R${:.2f} durante 2 meses'.format(nvalor))
elif condi == 4:
    print('3x ou mais vezes no cartão')
    p = int(input('Quantas vezes quer passar no cartão?'))
    juros = ((20/100 * valor) + valor) / p
    print('O novo valor é de R${:.2f} com juros por {} meses'.format(juros, p))
else:
    print("Código errado")
