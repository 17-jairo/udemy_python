'''
Reduce

OBS: A partir do Python3 a função reduce() não é mais uma função build-in. Agora temos que importar e utilizar esta fun
ção a partir do módulo 'functools.

Para entender o reduce()

# Imagine que voce tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E você tem uma função que recebe dois parametros:

def funcao(x, y):
    return x * y

Assim como map e filter, a função reduce recebe dois parametros: a função e o iteravel.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior.
No final reduce() irá retornar o resultado final.

Alternativamente poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

'''

# Como funciona na pratica?

# Vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parametros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# O que o reduce fara é primeiro acessar os dados '2 e 3, e vai aplicar na função, depois ele pega esse valor e aplica
# na função novamente, somando com o 4... e assim por diante... vai imprimir o resultado final