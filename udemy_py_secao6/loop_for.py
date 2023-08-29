"""
Loop for

Loop => Estrutura de repetição
For = > Faz parte de uma dessas estruturas

C ou Java

for(int i = 0; i < limitador; i++) {
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis.
Exemplos de iteráveis
- Strings:
    nome = "Geek University"
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1,10)

# Exemplo de for 1 (Iterando em uma String)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (Iterando sobre um Range)
for numero in numeros:
    print(numero)

for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome): (Quando não precisamos de um valor podemos descartar usando _)
    print(letra)

for valor in enumerate(nome):
    print(valor)

nome = 'Geek University'
lista = [1, 2, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista.

qtd = int(input("Quantas vezes esse loop deve rodar: "))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    soma = soma + num
print(f"A soma é {soma}")

dinamite = "Geek University"
for passaralho in dinamite:
    print(passaralho, end="")

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""
#Criando um loop de emojis
# Original: U+1FAE0
# Modificado: U0001FAE0

for num in range(1, 10):
    print('\U0001FAE0' * num)
