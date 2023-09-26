'''
Modulo Collections - Counter (Contador)

https://docs.python.org/3/library/collections.html

Collections - > High-performance Container Datatypes
Counter -> Recebe um interavel como parametro e cria um objeto do tipo Collection Counter que é parecido
com o dicionario, contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento
'''
# Realizando o import

from collections import Counter

# Podemos usar qualquer iteravel, aqui usamos uma lista

lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter

#Exemplo 1
res = Counter(lista)
print(type(res))
print(res)
# Exemplo 2
uni = Counter("Geek University")
print(uni)

#Exemplo 3

texto = ''' O Supremo Tribunal Federal (STF) formou maioria nesta quarta-feira (20) para invalidar a aplicação da tese 
do marco temporal na demarcação de terras indígenas. A formação da maioria é uma vitória para indígenas, 
que são contra a tese do marco temporal. A tese prevê que só podem ser demarcadas terras que já estavam sendo ocupadas 
por indígenas no dia 5 de outubro de 1988, data da promulgação da Constituição. Esse entendimento deriva de uma 
interpretação literal do artigo 231 da Constituição, que diz:'''

palavras = texto.split()
#print(palavras)

palavras2 = Counter(palavras)
print(palavras2)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(palavras2.most_common(5))

