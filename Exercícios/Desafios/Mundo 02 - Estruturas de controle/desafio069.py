i = p = s = m = 0
while True:
    print('='*30)
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()
    perg = str(input('Você deseja terminar? [S/N]')).strip().upper()
    p += 1
    if perg == 'S':
        break
    elif idade >= 18:
        i += 1
    elif sexo == 'M':
        s += 1
    elif sexo == 'F':
        if idade <= 20:
            m += 1
print(f'{p} se cadastraram, tem {i} pessoas com mais de 18 anos, tem {s} homens, {m} mulheres com menos de 20 anos')
print(i, s, m, p)
