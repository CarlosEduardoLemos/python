nome = input('Qual seu nome? ')
print('Bom em conhecer {}!'.format(nome))
print('Bom em conhecer {:^20}!'.format(nome))
print('Bom em conhecer {:=^20}'.format(nome))

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero: '))
som = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, a subtração é {}, o produto é {}'.format(som, sub, m), end=' ')
print('A divisão é {:.3f}, a divisão interia é {}, e potência {:.3f}'.format(d, di, e))
print('um teste \n para "aparecer" na tela')
