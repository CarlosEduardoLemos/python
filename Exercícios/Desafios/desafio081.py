c = 0
valores = list()
while True:
    n = int(input('digite um valor: '))
    valores.append(n)
    c += 1
    r = str(input('Você deseja adicionar mais um valor ?[S/N] '))
    if r == 'N' or r == 'n':
        break
print(f'Os valores digitados foram {valores} e a ordem decrescente é ', end='')
valores.sort(reverse=True)
print(valores, '!')
print(f'Você digitou {c} valores.')
if 5 in valores:
    print('Está na lista')
else:
    print('Não')
