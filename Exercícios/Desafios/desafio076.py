listagem = ('Lápis', 1.75,
'Borracha', 2,
'Caderno', 15.90,
'Estojo', 25,
'Transferidor', 4.20,
'Compasso', 9.99,
'Mochila', 99.99,
'Livro', 110)

print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R$ {listagem[pos]:>.2f}')
print('-' * 40)
