# Importando

from collections import namedtuple

# Precisamos definir o nome e parametros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow Chow', nome='Ray')

print(ray)
    #forma 1
print(ray[0])
print(ray[1])
print(ray[2])
    #forma2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow Chow'))
print(ray.count('Chow Chow'))
