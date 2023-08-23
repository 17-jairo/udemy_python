import random

a = random.randint(1, 100)
b = random.randint(1, 100)
contagem_acertos = 0
contagem_erros = 0

perg1 = int(input(f"1 - Qual é a soma de {a} + {b}, sendo que os numero a e b foram escolhidos aleatoriamente:  "))

if perg1 == (a + b):
    print("O valor está correto!")
    contagem_acertos += 1
else:
    print("O valor esta incorreto!")
    contagem_erros = 0

a = random.randint(1, 100)
b = random.randint(1, 100)

perg2 = int(input(f"2 - Qual é a soma de {a} + {b}, sendo que os numero a e b foram escolhidos aleatoriamente:  "))

if perg2 == (a + b):
    print("O valor está correto!")
    contagem_acertos += 1
else:
    print("O valor esta incorreto!")
    contagem_erros += 1

a = random.randint(1, 100)
b = random.randint(1, 100)

perg3 = int(input(f"3 - Qual é a soma de {a} + {b}, sendo que os numero a e b foram escolhidos aleatoriamente:  "))

if perg3 == (a + b):
    print("O valor está correto!")
    contagem_acertos += 1
else:
    print("O valor esta incorreto!")
    contagem_erros += 1

a = random.randint(1, 100)
b = random.randint(1, 100)

perg4 = int(input(f"4 - Qual é a soma de {a} + {b}, sendo que os numero a e b foram escolhidos aleatoriamente:  "))

if perg4 == (a + b):
    print("O valor está correto!")
    contagem_acertos += 1
else:
    print("O valor esta incorreto!")
    contagem_erros += 1

a = random.randint(1, 100)
b = random.randint(1, 100)

perg5 = int(input(f"5 - Qual é a soma de {a} + {b}, sendo que os numero a e b foram escolhidos aleatoriamente:  "))

if perg5 == (a + b):
    print("O valor está correto!")
    contagem_acertos += 1
else:
    print("O valor esta incorreto!")
    contagem_erros += 1

print(f"A quantidade de acertos foi {contagem_acertos} e a quantidade de erros foi {contagem_erros}")

"""
O codigo disponibilizado pelo chat gpt indica o uso de loopings, que ainda não foram aplicados neste curso.

import random

num_experimentos = 5  # Número de perguntas que você quer fazer
contagem_acertos = 0

for i in range(num_experimentos):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    
    resposta_correta = a + b
    
    perg = int(input(f"{i+1} - Qual é a soma de {a} + {b}, sendo que os números a e b foram escolhidos aleatoriamente: "))
    
    if perg == resposta_correta:
        print("O valor está correto!\n")
        contagem_acertos += 1
    else:
        print("O valor está incorreto!\n")

contagem_erros = num_experimentos - contagem_acertos

print("Resultados:")
print(f"Acertos: {contagem_acertos}")
print(f"Erros: {contagem_erros}")

"""


