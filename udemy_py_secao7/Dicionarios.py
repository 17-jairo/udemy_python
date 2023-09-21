'''
Dicionarios

Em algumas linguagens de programação os dicionarios python são conhecidos por mapas.
Dicionarios são coleções do tipo chave/valor.
Dicionarios são representados por chaves {}
--print(type({}))

# Criação de dicionarios

    # Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

    # Forma 2 (Menis comum)

paises = dict(br='Brasil', eua='Estados Unidos', py= "Paraguai")

print(paises)
print(type(paises))

# Acessando elementos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

    # Forma1 - Acessando via chave, da mesma forma que lista/tupla


print(paises['br'])
#print(paises['ru'])

    # Forma2 - Acessando via get - (recomendada)
print(paises.get('br'))
print(paises.get('ru'))
pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

print(paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive listas, tuple, dicionario

localidades = {
    (35.6895, 39.6917): 'Escritorio em Tókio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

print(receita)
print(type(receita))

    # Forma 1
receita['abr'] = 350
print(receita)

    #Forma2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionario

    # Forma 1
receita['mai'] = 550
print(receita)

    # Forma 2
receita.update({'mai': 660})
print(receita)
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Remover dados de um dicionário
    # Forma 1
ret = receita.pop('mar')
print(ret)
print(receita)

    # Forma 2
del receita['fev']

print(receita)
'''
'''
# Imagine que você tem um comércio eletronico, onde temos um carrinho de compras
# na qual adicionamos produtos

Carrinho de Compras:
    Produto 1:
        -nome;
        -quantidade;
        -preço;
    Produto 2:
        -nome;
        -quantidade;
        -preço;

 # 1 - Poderiamos utilizar uma lista para isso? sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

    # 2 - Poderiamos utilizar uma tupla para isso?

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.000)

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

    # 3 - Poderiamos utilizar um dicionario para isso?

carrinho1 = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 230.000}

produto2 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 150.000}
carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Métodos de dicionarios

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionario (zerar dados)

d.clear()
print(d)
# Copiando um dicionario para outro

    # Forma 1

novo = d.copy() # Deep Copy
print(novo)

novo['d'] = 4

print(d)
print(novo)

    # Forma 2 # Shallow Cody

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)
'''

# Forma não usual de criação de dicionarios usando fromkeys

outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}. fromkeys(['nome', 'pontos', ' email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

