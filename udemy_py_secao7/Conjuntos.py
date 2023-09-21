'''
Conjuntos

- Em qualquer linguagem de programação estamos fazendo referencia a
teoria de conjuntos da matematica.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja conjuntos não são indexaveis.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são refenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionarios) em Python:

    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

    # Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)
print(type(s))

# *OBS: Ao criar um conjunto, caso seja adicionado um valor já existente,
# será ignorado sem gerar error e não fará parte do conjunto.

    # Forma 2
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(lista, len(lista))
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(tupla, len(tupla))
dicionario = {}.fromkeys(lista, 'dict')
print(dicionario, len(dicionario))
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(conjunto, len(conjunto))

# Assim como outro conjunto Python podemos colocar tipos de dados misturados em Sets.

s= {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normal
for valor in s:
    print(valor
          )
# Usos interessantes com sets

    # Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museus,
    # e os visitantes informam manualmente a cidade de onde vieram.

    # Nós adicionamos cada cidade em uma cada cidade em uma lista python, ja que em uma lista podemos
    # adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)

    # Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos: (usando set):

cidades2 = set(cidades)
print(cidades2)

# Adicionando elementos em um conjunto
s= {1, 2, 3}
s.add(4)
s.add(4) # Duplicidade não gera erro, somente é ignorada
print(s)

# Remover elementos em um conjunto
    # Forma 1 (.remove)
s= {1, 2, 3}
s.remove(3) # Não remove o indice, sim o valor.
print(s)
    # Forma 2 (.discard)
s.discard(2)
print(s)

    # OBS: A diferença entre os dois é que no caso do .remove, caso seja solicitada a exclusão
    # de um numero inexistente no conjunto, ele imprimirá um KeyError. No caso do .discard nenhum erro é gerado.

#copiando um conjunto para outro...

s= {1, 2, 3}
print(s)

    # Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

 # Forma 2 - Shallow Copy

novo = s
novo.add(4)
print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s= {1, 2, 3}
print(s)
s.clear()
print(s)
______________________________________________________________________________
# Métodos matematicos de conjuntos

    # Imagine que temos dois conjuntos, um contendo estudantes de python e um com estudante de java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

    # Veja que alguns alunos que estudam Python também estudam Java.

    # Desafio: Precisamos criar um conjunto com nomes de estudantes unicos.

    # - Forma 1 (Union)

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

    # Forma 2 (Caractere pipe)

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos.

    # Forma 1 - Utilzando intersection

ambos1 = estudantes_python.intersection(estudantes_java)

    #Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)
print(ambos1)

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
so_java = estudantes_java.difference(estudantes_python)

print(so_java)
print(so_python)
'''










