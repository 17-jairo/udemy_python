'''
Funções com parametro Padrão (Default Parameters)

- Funções onde a passagem de parametro seja opcional;

# Exemplo de função onde a passagem de parametro seja opcional.
print('Geek University')

print()

# Exemplo de função onde a passagem de parametro seja obrigatória
def quadrado(numero)
    return numero **2

print(quadrado(3))
print(quadrado()) # TypeError


def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))
print(exponencial(3, 5))

#OBS
# Se o usuario passar somente 1 argumento, este será atribuido ao parametro numero, e será calculado o quadrado desse
# numero; Se o usuario passar 2 argumentos, o primeiro será atribuido ao parametro numero eo segundo ao parametro
# potencia. Então será calculada esta potencia.

# OBS: Em funções Python, os parametros com valores default(padrão) devem sempre estar ao final da declaração.

#ERRO
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos
def soma(num1, num2):
    return num1 +num2

print(soma(4, 3))
print(soma(4)) # Type error por que ele precisa que voce  adicione os dois argumentos
print(soma()) # Type error por que ele precisa que voce  adicione os dois argumentos

# Para ajustar esse problema, voce deve colocar um valor padrão para num1 e num2 na criação da variavel.

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return "Bem-vindo instrutor Geek"
    elif nome == "Geek":
        return "Eu pensei que você era o instrutor"
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao(nome='Ozzy'))

# Por que utilizar parametros com valor default?

- Nos permite ser mais flexiveis nas funções;
- Evita erros com parametros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parametros?
- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionarios, funções e etc:

# Exemplos:

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))
__________________________________________________________________________________________________________________
# Escopo - Evitar problemas e confusões...

# Variaveis globais
# Variaveis locais

instrutor = 'Geek'  # Variavel Global


def diz_oi():
    instrutor = 'Python'  # Variavel local
    return f'Oi {instrutor}'


print(diz_oi())

#OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local terá preferencia.

# ATENÇÃO com as variáveis globais (Se puder evitar, evite)

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError (A variavel local está sendo utilizada para processamento sem ter sido
    #inicializada
    return total
print(incrementa())
'''


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador

    return dentro()


print(fora())
print(fora())
print(fora())
