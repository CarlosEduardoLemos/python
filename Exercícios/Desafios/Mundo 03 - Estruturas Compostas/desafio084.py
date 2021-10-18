pessoas = list()
temp = list()
p = mai = men = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(int(input('Digite o peso: Kg')))
    if len(pessoas) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Deseja add mais alguem? [S/N]'))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {mai}Kg. Foi de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {men}Kg. Foi de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{men}', end='')
print()
