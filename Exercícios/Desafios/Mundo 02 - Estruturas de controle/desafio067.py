while True:
    print('-='*20)
    n = int(input('Digite um número: '))
    print('-='*20)
    if n < 0:
        break
    else:
        for tabuada in range(1, 11):
            print(f'{n} x {tabuada} = {n*tabuada}')
print('Obrigado e volte sempre !!')
print('-='*20)
