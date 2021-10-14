sex = ''
n = ''
F = M = 0
while n != 'S':
    sex = str(input('Digite "m" para Homens "f" para Mulheres.Se quiser sair digite s : ')).strip().upper()
    if sex == 'F':
        F = F + 1
    elif sex == 'M':
        M = M + 1
    elif sex == 'S':
        n = str(input('Tem certeza que quer sair? S para sair: ')).strip().upper()
    else:
        print('Erro')
print('tiveram {} homens e {} mulheres'.format(M, F))
print('Fim')
