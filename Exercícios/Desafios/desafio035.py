r1 = float(input('Qual o tamanho da reta 1? '))
r2 = float(input('Qual o tamanho da reta 2? '))
r3 = float(input('Qual o tamanho da reta 3? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo')
else:
    print('Os segmentos não podem formar um triângulo')
