import random
print('Pensei em um número entre 0 e 5, Tente adivinha')
num = int(input('Qual o número eu pensei? '))
n = random.randint(0, 5)
if num == n:
    print('Você acertou')
else:
    print('Você errou')
    print('Eu pensei em {}'.format(n))
