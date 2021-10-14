from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc=int(input('Digite o ano de nascimento: '))
    idade = atual - nasc
    if idade < 21:
        totmenor += 1
    elif idade >= 21:
        totmaior += 1
print('A quantidade de pessoas maiores de idade é: ', totmaior)
print('A quantidade de pessoas menores de idadde é:', totmenor)
