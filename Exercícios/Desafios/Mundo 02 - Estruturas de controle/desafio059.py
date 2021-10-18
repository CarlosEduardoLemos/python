n = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
from time import sleep
while n != 5:
    print('-'*20)
    print('Menu')
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos número
    [ 5 ] Sair do programa
    ''')
    print('-'*20)
    n = int(input('Digite o código: '))
    if n == 1:
        som = n1+n2
        print('O resultado da soma entre {} e {} é {}'.format(n1, n2, som))
    elif n == 2:
        multi = n1 * n2
        print('O resultado da multiplicação entre {} e {} é {}'.format(n1, n2, multi))
    elif n == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        elif n1 == n2:
            print('São iguais')
    elif n == 4:
        print('Novo número')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif n == 5:
        print('Finalizando...')
    elif n > 5 or n < 1:
        print('Código errado')
    sleep(2)
print('Fim do programa. Volte sempre.')
