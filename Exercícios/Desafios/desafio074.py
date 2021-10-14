from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os números sorteados foram {numeros}')
print(f'O menor valor é {sorted(numeros)[0]} e o mair valor é {sorted(numeros)[4]}')
#print(f'O menor valor é {min(numeros)} e o mair valor é {max(numeros)}')
