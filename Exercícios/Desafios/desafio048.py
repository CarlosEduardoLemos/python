soma = 0 #Variável acumulador
cont = 0 #Variável contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma dos {} valores é {}'.format(cont, soma))
