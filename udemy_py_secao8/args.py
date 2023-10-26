'''
Entendendo o *args

- O *args é um parametro como outro qualquer. Isso significa que voce podera chamar de qualquer coisa,
desde que comece com *

Exemplo:

*xis

Mas por convenção utilizamos *args para defini-lo

O que é *args?

O parametro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde já lembre-se que tuplas são imutaveis
______________________________________________________________________________________________________________
# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9)) # Utilizando o método de parametros padrão, ficaria muito dificil trabalhar com uma
# quantidade alta de dados.
_____________________________________________________________________________________________________________________
# Entendendo o args

def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))
___________________________________________________________________________________________________________________

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'University', "Geek"))
print (verifica_info(1, 'University', 3.145))
__________________________________________________________________________________________________________________
'''

def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador
print(soma_todos_numeros(*numeros)) # Use o asterisco para desempacotar listas como argumento, ou uma coleção.

