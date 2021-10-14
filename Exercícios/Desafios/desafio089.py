materias = list()
while True:
    aluno=str(input('Nome do aluno: '))
    n1=float(input('Nota 1: '))
    n2=float(input('Nota 2: '))
    media = (n1 + n2)/2
    materias.append([aluno, [n1, n2], media])
    resp=str(input('Deseja adicionar mais algum aluno? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8.1}')
print('-='*26)
for i, a in enumerate(materias):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*35)
    opc = int(input('Mostrar nota de qual aluno? (999 para sair):'))
    if opc == 999:
        break
    if opc <= len(materias)-1:
        print(f'Notas de {materias[opc][0]} são {materias[opc][1]}')
print('<<< Volte sempre >>>')
