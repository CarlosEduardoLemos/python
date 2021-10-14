def fatorial(numero, show=0):
    from math import factorial
    print(f'O fatorial de {numero} é {factorial(numero)}')
    if show==1:
        print('O cálculo desse fatorial é: ')
        for c in range(numero, 0, -1):
            print(f'{c}', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        print(factorial(numero))
    else:
        print('Cálculo não exibido')


numero = int(input('Informe um valor: '))
show = int(input('Deseja ver o cáculo desse fatorial? [0/1]'))
if show !=1 and show !=0:
    show=int(input('Opção inválida. Deseja ver o cálculo desse fatorial? [0/1]'))
fatorial(numero, show)
