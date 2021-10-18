from datetime import date
ano = int(input('Qual o ano de nascimento? '))
idade = date.today().year - ano
print(idade)
if idade <= 9:
    print('Categoria mirim')
elif idade >9 and idade <=14:
    print('Categoria infantil')
elif idade > 14 and idade <= 19:
    print('Categoria júnior')
elif idade > 19 and idade <= 25:
    print('Categoria sênior')
else:
    print('Categoria master')
