'''
N = int(input("Insert a positive number: "))
if N <= 0:
    print("Favor inserir numero inteiros positivos")
else:
    num = []
    numero = 1
    while len(num) < N:
        num.append(numero)
        numero += 1
maxi = max(num)
print(f"Os {N} primeiros números são: {num} e o maior deles é {maxi}")
'''

# Código fornecido pelo chatGPT, onde indicam o total erro com relação a maneira que eu pensei sobre o código.


# Solicita ao usuário a quantidade de números a serem lidos
n = int(input("Digite a quantidade de números a serem lidos: "))

# Verifica se n é maior que zero
if n <= 0:
    print("Por favor, insira uma quantidade válida de números positivos.")
else:
    # Inicializa variáveis para o maior número lido e a contagem
    maior_numero = None
    contagem = 0

    # Loop para ler os números e encontrar o maior
    for i in range(n):
        numero = float(input(f"Digite o número {i+1}: "))

        if i == 0 or numero > maior_numero:
            maior_numero = numero
            contagem = 1
        elif numero == maior_numero:
            contagem += 1

    # Imprime o maior número e a contagem
    print(f"O maior número lido foi {maior_numero} e ele foi lido {contagem} vezes.")

