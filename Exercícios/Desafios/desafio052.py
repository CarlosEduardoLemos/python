n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[m O número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('Logo, É primo')
else:
    print('Logo, Não é primo')
