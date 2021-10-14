somaidade = 0
mediaidade = 0
nomevelho = ''
maioridade = 0
totmulher = 0
for p in range(1, 5):
    print('----- {}ª pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip().lower().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média das idades é ', mediaidade)
print('O homem de maior idade é {} do {}'.format(maioridade, nomevelho))
print('O total de mulheres abaixo dos 20 anos é: ',totmulher)
