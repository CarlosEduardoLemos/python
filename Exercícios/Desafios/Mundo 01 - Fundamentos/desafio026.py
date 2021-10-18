algo = str(input('Digite algo: ')).strip()
print('A letra "A" aparece {} vezes'.format(algo.lower().count('a')))
print('A primeira aparição do "A" é {}'.format(algo.lower().find('a')+1))#o +1 é para ficar mais bonito para o usuário
print(' A última posição da letra "A" é {}'.format(algo.lower().rfind('a')+1))
