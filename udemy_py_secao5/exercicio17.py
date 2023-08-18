basemaior = float(input("Insira o valor da base maior: "))
basemenor = float(input("Insira o valor da base menor: "))
altura = float(input("Insira o valor da altura: "))

if 0 < basemaior and 0 < basemenor:
    a = (basemaior + basemenor) * altura / 2
    print(f"A área do trapézio é {a:.2f}")
else:
    print("Insira um número maior que 0.")
