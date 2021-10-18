print('='*30)
print('Campeonato Brasileiro 2019')
print('='*30)

equipe = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 
'Atlético Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 
'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará',
'Cruzeiro', 'CSA-Al', 'Chapecoense', 'Avaí')

print('Classificação: ')
print('')

for cont in range(0, len(equipe)):
    print(f'{cont+1}º {equipe[cont]}')
print('='*50)

print('Equipes em ordem alfabética:')
print(sorted(equipe))
print('='*50)

print('Os 5 Primeiros colocados são: ')
print(equipe[:5])
print('='*50)

print('Os 4 últimos colocados são: ')
print(equipe[-4:])
print('='*50)

print(f'O time Chapecoense está na {equipe.index("Chapecoense")+1}ª posição')
print('='*50)
