c = calc = 0
import random
while True:
    jogador = int(input('Digite um valor: '))
    esc = str(input('Digite Par ou Impar: ')).strip().lower().capitalize()
    computador = random.randint(0, 10)
    print(f'Sou seu computador, e eu escolhi o número {computador}')
    calc = jogador + computador
    if esc in 'Impar':
        if calc % 2 == 0:
            print(f'A soma entre {jogador} e {computador} é {calc} logo é par ')
            print('Você perdeu')
            break
        else:
            c += 1
            print(f'A soma entre {jogador} e {computador} é {calc} logo é impar ')
    if esc in 'Par':
        if calc % 2 != 0:
            print(f'A soma entre {jogador} e {computador} é {calc} logo é impar ')
            print('Você perdeu')
            break
        else:
            c += 1
            print(f'A soma entre {jogador} e {computador} é {calc} logo é par ')
print('Game Over !!', end=' ')
print(f'Você acertou {c} vezes seguidas')
