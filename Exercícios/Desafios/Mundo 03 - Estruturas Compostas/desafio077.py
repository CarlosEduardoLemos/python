palavras = ('programar', 'estudar', 'python', 'curso', 'video', 'aprender')
for p in palavras:
    print(f'\nNa palavra {p.capitalize()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
