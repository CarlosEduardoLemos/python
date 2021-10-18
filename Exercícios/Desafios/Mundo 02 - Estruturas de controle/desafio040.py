n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a sedunda nota: '))
média = (n1 + n2)/2
print(média)
if média < 5:
    print('Reprovado')
elif média >= 5 and média < 7:
    print('Recuperação')
elif média >= 7:
    print('Aprovado')
