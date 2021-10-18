menor = 0
maior = 0
for c in range(0, 5):
    peso = float(input('Digite o peso: '))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {} Kg'.format(maior))
print('O menor peso é {} Kg'.format(menor))
