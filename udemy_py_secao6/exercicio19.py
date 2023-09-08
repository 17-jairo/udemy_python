'''
num = int(input("Insert a positive number between 100 and 999: "))

if 100 <= num <= 999:
    traz = num
    while traz > 0:
        digito = traz % 10
        print(f"Dígito: {digito}")
        traz //= 10
else:
    print("Please, insert a number between 100 and 999!")
'''

numero = int(input("Digite um número inteiro entre 100 e 999: "))

if 100 <= numero <= 999:
    # Converte o número em uma string para iterar pelos dígitos
    numero_str = str(numero)

    for digito in numero_str:
        print(f"Dígito: {digito}")
else:
    print("Por favor, insira um número entre 100 e 999.")



