'''
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iteravel.

# Sintaxe da List Comprehension

[dado for dado in iteravel]

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in
       numeros]  # Para cada numero na lista numeros, multiplique por 10 e forme uma nova lista

print(res)

res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]

print(res)
-----------------------------------------------------------------------------------------------------------------------
# List Comprehension versus Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrado = numero * 2
    numeros_dobrados.append(numeros_dobrado)

print(numeros_dobrados)

# List Comprehension

print([numero * 2 for numero in numeros])

-----------------------------------------------------------------------------------------------------------------------
# Outros exemplos

# 1

nome = "Geek University"

print([letra.upper() for letra in nome])

# 2

amigos =['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos])

# 3

print([numero * 3 for numero in range(1,10)])
'''



