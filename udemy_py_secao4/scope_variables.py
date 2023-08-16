'''
Escopo de variaveis

Dois casos de escopo:

1 - Variaveis globais;
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa

2 - Variaveis Locais;
    -Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado
    ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

python é uma variavel de tipagem dinamica. Isso significa que ao declararmos uma variaveil,
nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesm

Exemplo em C
int numero = 42

Exemplo em Java:
int numero = 42

'''

numero = 42 # Exemple of global variable
print(numero)
print(type(numero))

numero = 2
if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)