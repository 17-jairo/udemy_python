numero = int(input("Digite um número inteiro de 4 dígitos (entre 1000 e 9999): "))

if 1000 <= numero <= 9999:
    # Convertendo o número em uma string para iterar sobre os dígitos
    numero_str = str(numero)

    for digito in numero_str:
        print(digito)
else:
    print("O número digitado está fora do intervalo válido.")
