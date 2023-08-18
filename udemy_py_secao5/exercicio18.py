inse1 = str(input("Escolha uma das operações abaixo: \n Soma \n Subtração \n Multiplicação \n Divisão \n Insira sua operação: "))
num1 = float(input("Insira o primeiro numero: "))
num2 = float(input('Insira o segundo numero: '))
if inse1 == "Soma":
    som = num1 + num2
    print(f"A soma é {som}")
elif inse1 == "Subtração":
    som = num1 - num2
    print(f"A subtração é {som}")
elif inse1 == "Multiplicação":
    som = num1 * num2
    print(f"A multiplicaçao é {som}")
elif inse1 == "Divisão":
    som = num1 / num2
    print(f"A divisão é {som}")
else:
    print("Coloque o nome da operação desejada considerando os exemplos sugeridos. ")


