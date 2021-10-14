números = (int(input('Digite um valor: ')), int(input('Digite o segundo valor: ')),
int(input('Digite o terceiro valor: ')), int(input('Digite o último valor: ')))
print(f'Os números digitados foram: {números}')
print(f'O número 9 apareceu {números.count(9)} vezes')
if 3 in números:
    print(f'O número 3 apareceu na {números.index(3)+1}ª posição')
else: 
    print('O número 3 não foi digitado em nenhuma posição')
print('Os números pares digitados foram: ', end='')
for n in números:
    if n % 2 ==0:
        print(n, end=' ')
