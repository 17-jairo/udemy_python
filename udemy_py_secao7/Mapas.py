'''
Conhecidos em python como dicionarios

#Interar com dicionarios
for chave in receitas: # Imprime as chaves
    print(chave)

for chave in receitas: # Imprime os valores
    print(receitas[chave])

# Acessando chaves
receitas = {'jan': 100, 'fev': 250, 'mar': 400}

print(receitas)
print(receitas.keys())

'''

receitas = {'jan': 100, 'fev': 250, 'mar': 400}

print(receitas)

# Acessando os valores

print(receitas.values())

for valor in receitas.values():
    print(valor)

# Desempacotamento de dicionários

for chave, valor in receitas.items():
    print(f'chave= {chave} e valor - {valor}')

# Soma, Valor maximo, Valor minimo, Tamanho

print(sum(receitas.values()))
print(max(receitas.values()))
print(min(receitas.values()))
print(len(receitas))

