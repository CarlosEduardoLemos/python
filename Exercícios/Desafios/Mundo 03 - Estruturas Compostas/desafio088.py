from random import randint
import time
sena = list()
jogo = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in sena:
            sena.append(num)
            cont += 1
        if cont >= 6:
            break
    sena.sort()
    jogo.append(sena[:])
    sena.clear()
    tot += 1
print('-='*30)
print(f'Sorteando {quant} jogos.')
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')
    time.sleep(0.5)
print('-='*30)
