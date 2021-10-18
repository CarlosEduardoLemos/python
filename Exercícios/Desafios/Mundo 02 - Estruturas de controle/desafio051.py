primeiro = int(input('Digite o primeiro termo: '))
razao= int(input('Digite o valor da razão: '))
décimo = primeiro + (10-1) * razao
for pa in range(primeiro, décimo, razao):
    print(pa)
