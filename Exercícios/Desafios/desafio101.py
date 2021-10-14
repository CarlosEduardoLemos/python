def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return print(f'Com {idade} anos: Não vota')
    elif 16<= idade < 18 or idade > 65:
        return print(f'Com {idade} anos: Voto opcional')
    else:
        return print(f'Com {idade} anos: Voto obrigatório')



ano = int(input('Ano de nascimento: '))
voto(ano)
