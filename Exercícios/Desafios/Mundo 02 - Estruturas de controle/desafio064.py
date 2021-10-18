num = 0
c = 0
som = 0
print('Se quiser sair digite 999!')
while num != 999:
   num = int(input('Digite um número: '))
   if num < 999 or num > 999:
       c += 1
       som = som + num
   elif num == 999:
       print('Você digitou {} valores e o resultado da soma de todos esses valores digitados é {}'.format(c, som))
print('Fim')
