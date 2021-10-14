num = int(input('Digite o valor para conversão: '))
print('1 - Binário')
print('2 - Octal')
print('3 - hexadecimal')
n = int(input('Para qual base quer converter? 1, 2 ou 3?'))
if n == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))
elif n == 2:
    print('O número {} em Octal é {}'.format(num, oct(num)[2:]))
elif n == 3:
    print('O numero {} em Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')

#fiz o fatiamento nas opções para mostrar o numero pois aparecia siglas referentes a conversão
