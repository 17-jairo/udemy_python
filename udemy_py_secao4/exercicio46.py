def inverter_digitos(numero):
    return int(str(numero)[::-1])


def main():
    numero = int(input("Digite um número inteiro de três dígitos (100 a 999): "))

    if 100 <= numero <= 999:
        novo_numero = inverter_digitos(numero)
        print(f"O novo número formado pelos dígitos invertidos é: {novo_numero}")
    else:
        print("Número fora do intervalo permitido.")


if __name__ == "__main__":
    main()
