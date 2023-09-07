N = int(input("Insira um numero inteiro positivo: "))
if N <= 0:
    print("Favor inserir numero inteiros positivos")
else:
    impares =[]
    numero = 1
    while len(impares) < N:
        if numero %2 != 0:
            impares.append(numero)
        numero += 1
print(f"Os {N} primeiros números naturais ímpares são: {impares}")

'''
Neste código:

Solicitamos ao usuário que insira um número inteiro positivo N.

Verificamos se N é maior que zero. Se não for, exibimos uma mensagem de erro.

Inicializamos uma lista vazia chamada impares para armazenar os números naturais ímpares.

Usamos um loop for para iterar de 1 até N * 2 (o * 2 garante que você obtenha pelo menos N números ímpares). O terceiro argumento do range é 2, o que faz com que o loop itere apenas pelos números ímpares.

Em cada iteração, adicionamos o número ímpar atual à lista impares.

Por fim, exibimos os primeiros N números naturais ímpares na lista impares.

Este código utilizará um loop for para imprimir os N primeiros números naturais ímpares, de acordo com o valor de N inserido pelo usuário.
'''