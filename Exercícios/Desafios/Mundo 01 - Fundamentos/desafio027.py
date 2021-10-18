nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('O primeiro nome é {}'.format(n[0]))
print('O último nome é {}'.format(n[len(n)-1]))
