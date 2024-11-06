from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

def removerUsuario(arq, nome):
    try:
        with open(arq, 'r') as file:
            linhas = file.readlines()
        with open(arq, 'w') as file:
            for linha in linhas:
                if nome not in linha:
                    file.write(linha)
        print(f'Usuário {nome} removido com sucesso.')
    except Exception as e:
        print(f'Erro ao remover usuário: {e}')

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Remover Usuário', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Remover usuário')
        nome = str(input('Nome do usuário a ser removido: '))
        removerUsuario(arq, nome)
    elif resposta == 4:
        cabeçalho('Saindo do Sistema...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)