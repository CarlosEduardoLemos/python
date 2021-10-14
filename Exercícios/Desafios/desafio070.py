total = menor = totmil = cont = 0
nome = ''
while True:
    prod = str(input('Nome do produto: ')).strip().lower().capitalize()
    valor = float(input('Valor do produto: R$'))
    cont += 1
    if cont == 1:
        menor = valor
        nome = prod
    else:
        if valor < menor:
            menor = valor
            nome = prod
    total += valor
    if valor > 1000:
        totmil += 1
    pedido = ''
    while 'S' not in pedido and 'N' not in pedido:
        pedido = str(input('Você que sair? [S/N]')).strip().upper()
    if pedido == 'S':
        break
print('Fim')
print(f'A conta total é de {total:.2f}')
print(f'Tem {totmil} produtos acima de R$1000,00')
print(f'O produto de menor valor foi {nome} no preço de {menor}')
