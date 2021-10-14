nome = str(input('Digite seu nome: ')).strip().lower()
if nome == 'carlos':
    print('Que nome lindo')
else:
    print('Que nome normal!')
print('bom dia flor do dia {}!'.format(nome.capitalize()))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('Sua média é {:.1f}'.format(m))
if m >= 6.0:
    print('Ótima nota, parabéns')
else:
    print('Fora da média, estude mais')
