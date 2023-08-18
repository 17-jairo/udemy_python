a = float(input("Insert the first side: "))
b = float(input("Insert the second side: "))
c = float(input("Insert the third side: "))

if c < (a + b) and b < (c + a) and a < (b + c):
    if a == b == c:
        print("É equilátero")
    elif a == b or a == c or c == b:
        print("É isósceles")
    else:
        print("É escaleno")
else:
    print("Não é um triângulo")

