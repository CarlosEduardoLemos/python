pessoas = {'nome': 'Carlos', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #dentro da formatação nesse casso coloca aspas duplas
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['nome'] = 'Benjamin'
pessoas['peso'] = 76.4
print(pessoas)

print('-='*30)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-=' * 30)

est = dict()
bras= list()
for c in range(0, 3):
    est['uf'] = str(input('Unidade federativa: '))
    est['sigla'] = str(input('Sigla do estado: '))
    bras.append(est.copy()) #no dicionário usa var.copy() para copiar, ja na lista e tuplas e var[:]
print(bras)
for e in bras:
    for v in e.values():
        print(v, end=' ')
    print()
