s = 'N'
c = som = maior = menor = 0
while s != 'S':
    num = int(input('Digite um número: '))
    c += 1
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    som = som + num
    s = str(input('Você quer sair? ')).strip().lower().capitalize()
result = som/c
print('Você digitou {} números, a soma entre esses números é {} e a média é {:.2f}'.format(c, som, result))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
