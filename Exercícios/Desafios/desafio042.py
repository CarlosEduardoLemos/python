r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triângulo', end=' ')
    if r1 == r2 == r3:
        print('equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('isóceles')
    else:
        print('escaleno')
else:
    print('Não forma um triângulo')
