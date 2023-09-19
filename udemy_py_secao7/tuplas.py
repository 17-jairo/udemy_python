'''
Tuplas (tuple)

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças

1 - As tuplas são representadas por parenteses.

2 - As tuplas são imutáveis: Isso significa que ao criar uma tupla ela não muda
Toda operação em uma tupla gera uma nova tupla
# ATENCAO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# ATENCAO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4, ) # Isso é uma tupla!
print(tupla4)

print(type(tupla4))

# CONCLUSAO: Podemos concluir que tuplas são definidas pela virgula, não pelo parenteses.

# Tuplas tambem podem ser criadas através de ranges.
tupla =tuple(range(11))
print(tupla)
print(type(tupla))


#Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla

print(escola)
print(curso)
# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis

# Soma, Valor maximo, valor minimo e tamanho

tupla = tuple(range(11))
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla2 + tupla1) # Tuplas são imultaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(33 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
i = 0
while i < len(meses):
    print(meses([i]))
    i = i + 1

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utilização de tuplas

    # Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# verificamos em qual elemento esta na tupla

print(meses.index('Junho'))

# Slicing
    #tupla[inicio:fim:passo]

print(meses[5:9])

# Por que utilizar tuplas?
    # Tuplas são mais rapidas que listas
    # Tuplas deixam seu código mais seguro

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)
nova = tupla
print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
'''



