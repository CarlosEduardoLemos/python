sal = float(input('Digite o salário do funcionário: R$ '))
if sal > 1250.00:
    aumento = ((10/100)*sal) + sal
    print('Seu novo salário é R${:.2f}'.format(aumento))
if sal <= 1250.00:
    aumento = ((15/100)*sal) + sal
    print('Seu novo salário é de R${:.2f}'.format(aumento))
