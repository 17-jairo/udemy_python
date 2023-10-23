'''
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Funções em python que retornam valores devem retornar estes valores com a palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno
de uma função. Podemos passar a execução da função para outras funções

# Exemplo função

# Vamos refatorar esta função para que ela retorne
def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(f'Retorno {ret}')
print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira função
def diz_oi():
    return "Oi "


alguem = "Pedro!"
print(diz_oi() + alguem)

Obs: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores

# Exemplo 1

def diz_oi():
    return 'Oi!'
    print('Estou sendo executado após o retorno') # Após o retorno, nada é executado!
print(diz_oi())

# Exemplo 2
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 3
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

# vamos criar uma função para jogar a moeda

from random import random
def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
'''

# Erros comuns na utilização do retorno, que na verdade são codificações desnecessárias

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    else: # Esse else não é necessário quando voce tem duas respostas possiveis. Veja abaixo
        return False
print(eh_impar())

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False # Basta escrever a função return abaixo da outra função return
print(eh_impar())
