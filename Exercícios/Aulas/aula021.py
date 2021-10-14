help(print)
print('=' * 90)
print(input.__doc__)

#parametro opcional
def contador(i, f, p):
    """
    
    :param i:
    :param f:
    :param p:
    :return:
    """
    c=i
    while c <= f:
        print(f'{c}', end='..')
        c+=p #incremento
    print('Fim!!')


contador(2, 10, 2)
help(contador)
print('=' * 30)


def somar(a=0, b=0, c=0):
    """
    
    :param a: o primeiro valor 
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: 
    Função criada por carlos
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 4, 1)
somar(2, 5)
somar()
help(somar)

#escopo de variáveis

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
# O valor de x tem um escopo local, já o valor de n tem o escopo global. Se eu colocar um print de x no programa local vai dar erro.

print('=' * 30)
#retorno de valores
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 4, 1)
r2 = somar(2, 5)
r3 = somar()
print(f'Os resultados foram {r1}, {r2}, {r3}')


print('+' * 20)


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os valores são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('É impar')
