alunos = dict()
alunos['Nome'] = str(input('Nome do aluno: '))
alunos['Média'] = float(input('Média do aluno: '))
if alunos['Média'] >= 5:
    alunos['Situação'] = 'Aprovado'
else:
    alunos['Situação'] = 'Reprovado'
print(alunos)
