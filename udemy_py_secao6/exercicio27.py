num1 = int(input("Insert a positive number: "))
soma = 0
for ramb in range(1, num1 + 1):
    h = 1/ramb
    soma += h
print(f"The {num1} is {soma:.2f} ")

# Versão do código usando While:

num1 = int(input("Digite um número positivo: "))
soma = 0
ramb = 1

while ramb <= num1:
    h = 1 / ramb
    soma += h
    ramb += 1

print(f"A soma da série harmônica para n = {num1} é aproximadamente {soma:.2f}")
