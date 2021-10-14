from random import randint
from time import sleep

print('''[0] Pedra
[1] Papel
[2] Tesoura
''')

jogador = int(input('Qual a sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Jo')
sleep(1)
print('ken')
sleep(1)
print('pô!!!')

if computador == 0:
    print('-='*11)
    print('O computador jogou', itens[0])
    if jogador == 0:
        print('Você escolheu', itens[0])
        print('-=' * 11)
        print('Empate')
    elif jogador == 1:
        print('Você escolheu', itens[1])
        print('-=' * 11)
        print('Jogador ganhou')
    elif jogador == 2:
        print('Você escolheu', itens[2])
        print('-=' * 11)
        print('O computador ganhou')
    else:
        print('Sua opção é inválida')

elif computador == 1:
    print('-=' * 11)
    print('O computador jogou', itens[1])
    if jogador == 0:
        print('Você escolheu', itens[0])
        print('-=' * 11)
        print('O computador ganhou')
    elif jogador == 1:
        print('Você escolheu', itens[1])
        print('-=' * 11)
        print('Empate')
    elif jogador == 2:
        print('Você escolheu', itens[2])
        print('-=' * 11)
        print('O jogador ganhou')
    else:
        print('Sua opção é inválida')

elif computador == 2:
    print('-=' * 11)
    print('O computador jogou', itens[2])
    if jogador == 0:
        print('Você escolheu', itens[0])
        print('-=' * 11)
        print('O jogador ganhou')
    elif jogador == 1:
        print('Você escolheu', itens[1])
        print('-=' * 11)
        print('O jogador perdeu')
    elif jogador == 2:
        print('Você escolheu', itens[2])
        print('-=' * 11)
        print('Empate')
    else:
        print('Sua opção é inválida')
