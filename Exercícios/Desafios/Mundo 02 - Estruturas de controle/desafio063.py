elem = int(input(('Digite quantos termos quer que apareça: ')))
t1 = 0
t2 = 1
cont = 3
print('{} -> {}'.format(t1, t2), end='')
while cont <= elem:
    t3 = t1+t2
    cont += 1
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' -> Fim')
