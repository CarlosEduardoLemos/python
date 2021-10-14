soma = 0
for par in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = n + soma
        print('O número {} é par'.format(n))
print('A soma dos pares é {}'.format(soma))
