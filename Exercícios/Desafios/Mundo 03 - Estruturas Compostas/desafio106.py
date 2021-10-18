#Programa que faz acesso ao pyhelp.
from time import sleep
#Menu de cores
c = (
    '\033[m',       #0 - Sem cor
    '\033[0;30;41m', #1 - Vermelho
    '\033[0;30;42m', #2 - Verde
    '\033[0;30;43m', #3 - Amarelo
    '\033[0;30;44m', #4 - Azul
    '\033[0;30;45m', #5 - Roxo
    '\033[7;30m',   #6 - Branco
)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


#Programa que edita o titulo
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa principal
comando = ''
while True:
    titulo('    Sistema de ajuda PyHELP', 2)
    comando=str(input("Função ou biblioteca>"))
    if comando.upper() == 'Fim':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
