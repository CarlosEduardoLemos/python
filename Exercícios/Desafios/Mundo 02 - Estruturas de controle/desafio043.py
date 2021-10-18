alt = float(input('Didite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (alt * alt)
print('O seu IMC é de {:.2f}'.format(imc))
if imc < 25:
    print('Abaixo do peso')
elif imc >= 25.0 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 30.0 and imc <=34.9:
    print('Obesidade grau 1')
elif imc >= 35.0 and imc <= 39.9:
    print('Obesidade 2')
elif imc > 40:
    print('Obesidade 3')
