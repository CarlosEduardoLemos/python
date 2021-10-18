from datetime import datetime
trabalho = dict()
trabalho['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
trabalho['Idade'] = datetime.now().year - nasc
trabalho['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalho['ctps'] != 0:
    trabalho['Contratação'] = int(input('Ano de contratação: '))
    trabalho['Salário'] = float(input('Salário: R$'))
    trabalho['Aposentadoria'] = trabalho['Idade'] + ((trabalho['Contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in trabalho.items():
    print(f'{k} recebe {v}')
