try:
    a = int(input('Numerador: '))
    b = int(input('Denominaador: '))
    r = a / b
#except:
#    print('infelizmente deu erro :(')
#except Exception as erro:
#    print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except ZeroDivisionError:
    print('Não é possivel dividir um númeor por zero!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado')
