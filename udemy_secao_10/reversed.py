'''
Reversed

OBS: Não confunda com a função reverse que estudamos nas listas. O reversed pode ser usado em todas as situações
'''

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Set
print(set(reversed(lista)))

# Podemos iterar sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end='')
print('\n')

# podemos fazer o mesmo sem o uso do for

print(''.join(list(reversed('Geek University'))))

