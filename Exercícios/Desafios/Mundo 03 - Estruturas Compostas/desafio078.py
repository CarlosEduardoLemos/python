valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
print(f'O maior valor é {max(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i + 1}...', end=' ')
print()
print(f'O menor valor é {min(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i + 1}...', end=' ')
print()
