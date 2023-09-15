'''
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens,
com a diferença de serem dinamicos e também de poder colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamanho fixo: Ou seja, podemos criar a lista e simplesmente ir adicionando
elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dados.
- As listas em Python são representadas por colchetes [].




# Podemos facilmente identificar se determinado valor esta contido na lista.
num = 7
if num in lista4:
    print(f"Encontrei o numero {num}")
else:
    print(f"Não encontrei o numero {num}")

# Podemos facilmente coordenar uma lista (método .sort())

lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista (método .count)

print(lista1.count((1)))
print(lista5.count('e'))

# Podemos adicionar elementos em listas (método .append())

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1]) # Nesse caso, será adicionado essa lista dentro da lista principal.
print(lista1)

# Para adicionar mais de um elemento ao final da lista, deve-se usar o método .extend()

lista1.extend([123, 44, 67])
print(lista1)

O extend pode ser usado também para adicionar outra lista numa lista já pré existente.
lista1.extend(lista2)
print(lista1)

lista1.extend(lista2)
print(lista1)

# Pode-se inserir um nove elemento na lista informando a posição do indice, usando o método .insert()

lista1.insert(2, 'Novo valor')
print(lista1)

# Pode-se juntar facilmente duas listas

lista6 = lista1 + lista2
print(lista6)

# Para imprimir os itens da lista ao contrario, deve-se usar o método .reverse()

lista1.reverse() # Seria como usar o split: lista1[::-1]
lista2.reverse() # Seria como usar o split: lista1[::-1]

print(lista1)
print(lista2)

# Para copiar uma lista, deve-se usar o método .copy()

lista6 = lista2.copy()
print(lista6)

# Para saber o tamanho de uma lista, deve-se utilizar a função len.

print(len(lista6))

# Para remover facilmente o ultimo elemento de uma lista, deve-se usar o método .pop()

print(lista5)
lista5.pop()
print(lista5)
    # Podemos remover um elemento pelo indice (Caso não tenhamos elemento no indice informado, teremos o erro IndexError
lista5.pop(2) # Os elementos à direita deste indice serão deslocados para esquerda.
print(lista5)

# Podemos remover todos os elementos (zerar a lista) usando o método
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos converter uma string para uma lista usando .split()
    # Exemplo 1
curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split() # Por padrão o split separa os elementos da lista pelo espaço entre elas.
print(curso)

    # Exemplo 2
curso = 'Programação,em,python:,Essencial'
print(curso)
curso = curso.split(',') # Por padrão o split separa os elementos da lista pelo espaço entre elas.
print(curso)

# Convertendo uma lista em string
lista6 = ['Programação', 'em', 'python:', 'Essencial']
print(lista6)
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', [1, 2, 3], 45345345345]
print(lista6)
print(type(lista6))

# Iterando sobre listas

    # Exemplo1 - Utilizando for
soma = 0
for elemento in lista2: #Dessa maneira ele imprime e itera dentro dos elementos da lista.
    print(elemento)
    soma = soma + elemento
print(soma)

    # Exemplo2 - Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

    # Para fazer o acesso inverso
print(cores[-1])

    # Usando for
for cor in cores:
    print(cor)

    # Usando While
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cor in enumerate(cores):
    print(indice, cor)

# Outros métodos não tão importantes mas também úteis

# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

    # Em qual índice da lista está o valor 6?
print(numeros.index(6))
    # Em qual índice da lista está o valor 9?
print(numeros.index(9))
    # OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))
    # Podemos fazer a busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1)) # Buscando a partir do indice 1
print(numeros.index(5, 2)) # Buscando a partir do indice 2
print(numeros.index(5, 3)) # Buscando a partir do indice 3
print(numeros.index(5, 4)) # Buscando a partir do indice 4

    # Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) #Busca pelo indice valor 8, entre os indices 3 e 6.

# Trabalhando com slice de lista com o parametro

    # lista[inicio:fim:passo]
    #range(inicio:fim:passo)
lista = [1, 2, 3, 4]

print(lista[1:])
print(lista[:2])
print(lista[:4])
print(lista[1:3])

# Trabalhando com slice de lista com parametro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2

print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2.

# Invertendo valores de uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1], = nomes[1], nomes[0]

print(nomes)

nomes.reverse()
print(nomes)

# Soma, Valor Maximo, Valor Mínimo

    # Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista)) # maximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista

# Transformando lista em tupla

tupla = tuple(lista1)
print(tupla)

# Desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)
'''
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list("Geek University")

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 (Deep Copy) Quando uma lista nova não altera a anterior

lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)
nova = lista #Shallow copy
print(nova)
nova.append(4)
print(lista)
print(nova)





