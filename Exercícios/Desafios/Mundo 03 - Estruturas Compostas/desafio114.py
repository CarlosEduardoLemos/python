import urllib
import urllib.request

print('\033[0;31m Lembrando que a URL deve ser digitada a partir do htpps ou htpp \033[m')
s = str(input('Digite a URL do site: '))
try:
    site = urllib.request.urlopen(s)
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso!')

'''
O exercício era para verificar se um site com a URL: http://pudim.com.br estava no ar, mas dei uma "Modificada" para poder verificar qualquer URL.
'''