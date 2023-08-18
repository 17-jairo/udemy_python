def soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

numero = int(input("Digite um número inteiro maior do que zero: "))

if numero > 0:
    resultado = soma_digitos(numero)
    print(f"A soma dos dígitos de {numero} é {resultado}.")
else:
    print("Número não válido.")
