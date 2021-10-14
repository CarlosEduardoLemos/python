def escreva(palavra):
    tam = len(palavra) + 4
    print('=' * tam)
    print(f'  {palavra}')
    print('=' * tam)


palavra = str(input('Digite algo: '))
escreva(palavra)
