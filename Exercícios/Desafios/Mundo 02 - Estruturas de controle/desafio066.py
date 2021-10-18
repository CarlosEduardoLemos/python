soma = c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Foram digitados {c} números e a soma dos valores é de {soma}')
