teste = list()
print('-='*15)
teste.append('Carlos')
teste.append(22)
galera = list()
galera.append(teste)
print(galera)
"""
No caso abaixo vai aparecer duas marias com 32. O porque é que quando só faz um append está fazendo uma ligação entre as duas estruturas.
Para não ter essa ligação precisa fazer uma cópia. Para fazer uma cópia é preciso colocar após o teste colocar chaves "[]" e dentro dessas
chaves colocar o sinal de pontuação dois pontos.
"""
#galera.append(teste)
#teste[0] = 'Maria'
#teste[1] = 32
#print(galera)

galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 32
print(galera)

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Márcia', 45]]
print(pessoas)
print(pessoas[0])
print(pessoas[2][1])
print('-='*15)
for p in pessoas:
    print(p)
print('-='*15)
for p in pessoas:
    print(p[0])
print('-='*15)
for p in pessoas:
    print(p[1])
print('-='*15)
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-='*15)

humanos = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(str(input('Idade: ')))
    humanos.append(dados[:])#Se não tivesse as chaves e os dois pontos dentro das chaves iria aparecer so chaves por causa do clear escrito abaixo
    dados.clear()
print(humanos)
print('-='*15)
'''
for p in humanos:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idades')
print('-='*15)
'''
