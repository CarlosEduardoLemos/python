lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Bata Frita')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
pessoa = ('Carlos', 22, 'M', 110.23)# A tupla é um vetor comparada com outras linguagens mas no python pode colocar numeros e str

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) #Sorted coloca em ordem alfabética mas não modifica a tupla
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[-2:])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:3])

print(a)
print(b)
print(c)
print (d)
print(d.index(5))
print(d.index(5, 1))

print(pessoa)
del(pessoa)#Deleta a tupla
#print(pessoa)#Já que deleita a tupla pessoa acima, no termonal vai aparecer que não existe a tupla pessoa
