'''
Modulo Collections - Default Dict

https://docs.python.org/3/library/collections.html

# Recapitulando dicionario:

dicionari0 = {'curso': 'Programaçao em Python: Essencial'}
print(dicionari0)
print(dicionari0['curso'])
print(dicionari0['outro']) # Vai dar key error

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome, que podem ou não receber parametros de entrada
e retornar valores.
'''
# Fazendo o Import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['outro']) # Aqui seria um KeyError no dicionario comum, mas não aqui
print(dicionario)
