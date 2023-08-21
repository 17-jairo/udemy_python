valor = float(input("Insert the price tag value: "))
estado = str(input("Insert the delivered province: "))
estado1 = str.upper(estado)
if estado1 == "MG":
    tax1 = valor * 1.07
    print(f"The final value added taxes is R$ {tax1:.2f} for Minas Gerais!")
elif estado1 == "SP":
    tax2 = valor * 1.12
    print(f"The final value added taxes is R$ {tax2:.2f} for São Paulo!")
elif estado1 == "RJ":
    tax3 = valor * 1.15
    print(f"The final value added taxes is R$ {tax3:.2f} for Rio de Janeiro!")
elif estado1 == "MS":
    tax4 = valor * 1.08
    print(f"The final value added taxes is R$ {tax4:.2f} for Mato Grosso!")
else:
    print("Please insert a valuable province code, like 'mg, SP, rj, MS'! ")
