#Passagem sem parâmetro
def lin():
    print('-' * 30)


print('-' * 30)
print('Curso em vídeo')
print('-' * 30)
print('Python')
print('-' * 30)

#Programa com a função criada, chamada lin():
lin()
print('Curso em video')
lin()
print('Python')
lin()

#Passando por parâmetro:
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


título('Curso em vídeo')
título('Python é muito bom')
título('Oi')


a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)

print()


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)

print()


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print()

def dobra (lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)

print()

def conta(* contar):
    qw = 0
    for num in contar:
        qw += num
    print(f'Somando os valores {contar} temos {qw}')


conta(5, 2)
conta(2, 9, 4)
