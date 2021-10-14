from random import randint

numeros = list()


def sorteio():
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
    print(f'números sorteados: {numeros}')


def somePar():
    s = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            s += v
    print(f'A soma dos pares digitados {numeros} é {s}')


print('=' * 35)
sorteio()
print('=' * 35)
print('=' * 50)
somePar()
print('=' * 50)
