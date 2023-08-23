altura = float(input("Insira a sua altura: "))
peso = float(input("Insira seu peso: "))

if altura < 1.20 and peso <= 60:
    print("Grupo A!")
elif 1.20 < altura < 1.70 and peso <= 60:
    print("Grupo B!")
elif altura > 1.70 and peso <= 60:
    print("Grupo C!")
elif altura < 1.20 and 60 <= peso <= 90:
    print("Grupo D!")
elif 1.20 < altura < 1.70 and 60 <= peso <= 90:
    print("Grupo E!")
elif altura > 1.70 and 60 <= peso <= 90:
    print("Grupo F!")
elif altura < 1.20 and peso >= 90:
    print("Grupo E!")
elif 1.20 < altura < 1.70 and peso >= 90:
    print("Grupo E!")
elif altura > 1.70 and peso >= 90:
    print("Grupo E!")
else:
    print("Valor invalido!")

"""
Código errado, devido a sublocação das condicionais:
Correção chat gpt:
altura = float(input("Insira a sua altura: "))
peso = float(input("Insira seu peso: "))

if altura < 1.20:
    if peso <= 60:
        print("Grupo A!")
    elif 60 <= peso <= 90:
        print("Grupo D!")
    else:
        print("Grupo E!")
elif 1.20 <= altura < 1.70:
    if peso <= 60:
        print("Grupo B!")
    elif 60 <= peso <= 90:
        print("Grupo E!")
    else:
        print("Grupo E!")
elif altura >= 1.70:
    if peso <= 60:
        print("Grupo C!")
    elif 60 <= peso <= 90:
        print("Grupo F!")
    else:
        print("Grupo E!")
else:
    print("Valor inválido!")
"""