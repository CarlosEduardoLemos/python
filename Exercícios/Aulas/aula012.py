nome = str(input('Digite seu nome: ')).strip().lower()
if nome == 'carlos':
    print('Que nome bonito')
elif nome == 'lucas' or nome == 'maria' or nome == 'pedro':
    print('Seu nome é bem popular no Brazil.')
elif nome in 'ana cláudia carla júlia':
    print('Belo nome feminino')
elif nome in 'jéssica':
    print('Já acabou {}'.format(nome.capitalize()))
else:
    print('Seu nome é bem normal.')
print('Tenha um ótimo dia, {}!'.format(nome.capitalize()))
