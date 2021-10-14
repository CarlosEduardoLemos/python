num = [2, 9, 4, 7, 9, 3, 4, 9]
print(num)
num[2] = 3 #Modifiquei o valor que está no indice 2
print(num)
print(f'Essa lista tem {len(num)} elementos')
#num[4] = 5 Dessa forma da erro pois não é assim que add ou modifica o indice que não existe
num.append(5) #Dessa maneira que add algum valor na lista.
print(num)
num.sort() #Coloquei em ordem crescente, A partit de agora quando for mostrar a lista vai aparecer dessa forma
print(num)
num.sort(reverse=True) #Colocando do maior para o menor
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.insert(2, 0) #Add o valor 0 no indice que escolhi que é o indice 2
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop() #Como não coloquei nenhum parâmetro, vai remover o último valor
print(num)
num.pop(2) #Retirei o valor que estava no indice 2
print(num)
num.remove(9) #nesse ele remove o parametro que passei no primeiro valor que aparecer na lista
print(num)
if 10 in num:
    num.remove(10)
else:
    print('Não achei o número 10')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista.')

a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8 #Como a e b estão igualados, o que acontece em um acontece no outro
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b = a[:]#nesse caso o b é uma copia.
b[2] = 16#ja que b é uma cópia do a as mudanças feitas no b não interfere no a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
