a = 3
b = 5
nome = str(input('Digite seu nome: '))
print('Os valores são \033[31m{}\033[m e \033[32m{}\033[m !!!'.format(a, b))
print('Olá! Muito prazer em te conhecer {}{}{} !!!'.format('\033[4;34m', nome, '\033[m'))
