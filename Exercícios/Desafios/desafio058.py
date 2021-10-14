p = 0
tent = 0
from random import randint
from time import sleep
n = (randint(0, 10))
print('pensei em um número. Tente adivinhar.')
while p != n:
   p = int(input('Seu palpite: '))
   tent += 1
   print('Analisando...')
   sleep(0.3)
   if p > n:
       print('menos, tente outra vez')
   if p < n:
       print('Mais, tente outra vez')
print('Parabéns, Eu pensei no número ', n)
print('Você acertou em {} tentativas'.format(tent))
