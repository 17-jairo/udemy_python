'''
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatisticos

import statistics

# Dados coletados de um sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)
print(f"Média: {media}")
#OBS: Assim como a função map(), a filter() recebe dois parametros, sendo uma função iteravel

res = filter(lambda x: x > media, dados)
print(list(res))

#OBS: Assim como na função map, após ser utilizado os dados de filter, eles serão excluidos da memória
_______________________________________________________________________________________________________________________
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# Forma 1 - Mais simples
res = filter(None, paises) # Fazer um filtro tirando os vazios (none) da lista paises

# Forma 2 - com lambda e len
res = filter(lambda pais: len(pais) > 0, paises) # Fazer um filtro considerando todos os paises que tem mais que 0 letra

# Forma 3 - com lambda e diferença !=
res = filter(lambda pais: pais != '', paises) # Fazer um filtro considerando todos os paises diferentes de " "

print(list(res))

# A diferença entre map() e filter() é:

# map() - Recebe dois parametros, uma função e um iteravel e retorna um objeto mapeando a função para cada elemento

# filter() - Recebe dois parametros uma função e um iteravel e retorna um objeto filtrando apenas os elementos.
-----------------------------------------------------------------------------------------------------------------------
# Exemplo mais complexo

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Eu vou sair hoje']},
    {'username': 'gal', 'tweets': []}
]

print(usuarios)
# Forma 1 - filtra pelos usuarios que tem o tweet de tamanho 0
# inativos = list(filter(lambda usuario: len(usuario['tweets'])== 0, usuarios))

# Forma 2 - filtra os usuarios que não tem nada escritos em tweets
#inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)
'''

# Combinar filter () e map ()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

