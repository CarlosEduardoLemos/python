from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    diferença = 18 - idade
    print('Você irá se alista daqui {} anos'.format(diferença))
elif idade == 18:
    print('Você deverá comparecer a junta militar')
elif idade > 18:
    diferença = idade - 18
    print('Tem {} anos que você se alistou'.format(diferença))
