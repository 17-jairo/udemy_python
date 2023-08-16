'''
Estruturas lógicas: and, or, not, is

Operadores unários:
    not,
Operadores binários:
    and, or, is

And: Ambos os valores precisam ser True
Or: Um ou outro valor precisa ser True
Not: O valor do booleano é invertido, ou seja, se for true vira false, se for false vira true
Is: O valor é comparado com o segundo.
'''

ativo = True
logado = False

if ativo:
    print('Bem vindo usuario')
else:
    print('Ative sua conta!')

# ativo é verdadeiro?
print(ativo is True)