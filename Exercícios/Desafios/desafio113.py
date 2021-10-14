def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print('\033[0;31mErro! Digite um número válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuário não quis digitar')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except(TypeError, ValueError):
            print('\033[0;31mErro! Digite um número válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuário não quis digitar')
            return 0
        else:
            return n


n=leiaInt('Digite um número inteiro: ')
n1=leiaFloat('Digite um número Real: ')
print(f'O Valor inteiro digitado {n} e o valor Real Digitado {n1}')
