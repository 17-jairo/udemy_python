'''
Generators

Em aulas anteriores, foi estudado:
- List Comprehension,
- Dictionary
- Set Comprehension

Não vimos
- Tuple Comprehension - pois elas se chamam generators
-----------------------------------------------------------------------------------------------------------------------
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

# A diferença entre List comprehension e generator tem a ver com o uso de memória, muito mais utilizavel com generator
'''

from sys import getsizeof

# Gerando uma lista de numeros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dictonary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Generator
gen = getsizeof(( x * 10 for x in range(1000)))

print(" Para fazer a mesma atividade, gastamos em memória: ")
print(f'List comprehension: {list_comp} bytes')
print(f'Set comprehension: {set_comp} bytes')
print(f'Dict comprehension: {dic_comp} bytes')
print(f'Generator: {gen} bytes')