num1 = float(input("Insert the price: "))

if num1 < 50:
    porc1 = num1 * 1.05
    if porc1 < 80:
        print(f"O valor atualizado é {porc1:.2f} e o produto é considerado BARATO.")
elif 50 <= num1 < 100:
    porc2 = num1 * 1.10
    if 80 <= porc2 <= 120:
        print(f"O valor atualizado é {porc2:.2f} e o produto é considerado NORMAL.")
    else:
        print(f"O valor atualizado é {porc2:.2f} e o produto é considerado BARATO.")
elif 100 <= num1:
    porc3 = num1 * 1.15
    if 120 <= porc3 <= 200:
        print(f"O valor atualizado é {porc3:.2f} e o produto é considerado CARO.")
    elif 200 < porc3:
        print(f"O valor atualizado é {porc3:.2f} e o produto é considerado MUITO CARO.")
    else:
        print(f"O valor atualizado é {porc3:.2f} e o produto é considerado NORMAL.")
else:
    print("Seu numero esta valido, digite novamente!")
