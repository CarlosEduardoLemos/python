from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
ranking = list()
for c in range(0, 4):
     jogadores[f'jogador {c + 1}']=randint(1, 6)
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
