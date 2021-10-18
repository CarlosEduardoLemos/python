valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Deseja adicionar mais números? [S/N]'))
    if resp in 'Nn':
        break
print(f'Os valores digitados foram {valores}')
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os pares digitados foram {pares}')
print(f'Os impares digitados foram {impares}')
