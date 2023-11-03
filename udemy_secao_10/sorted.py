'''
Sorted

Não confunda com a função sort que já estudamos em listas. O sort() só funciona em listas. Podemos utilizar o sorted()
com qualquer iteravel

Como o próprio nome diz, sorted() serve para ordenar.
-----------------------------------------------------------------------------------------------------------------------
numeros = [6, 1, 8, 2]

print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior

print(numeros)
-----------------------------------------------------------------------------------------------------------------------
numeros = [6, 1, 8, 2]

# Adicionando parametros ao soted()

print(sorted(numeros, reverse=True)) # Ordena e inverte a lista
-----------------------------------------------------------------------------------------------------------------------
# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Eu vou sair hoje']},
    {'username': 'gal', 'tweets': []}
]

print(usuarios)
# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))
'''

# Ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dark Skin Mask", "tocou": 2},
    {"titulo": "Back in black", "tocou": 4},
    {"titulo": "Gatorade vencido", "tocou": 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))