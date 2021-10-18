numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 
'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente novamente.', end=' ')
    elif num >=0 and num <=20: 
        print(f'O numero {num} digitado em extenso é {numeros[num]}.')
        break
