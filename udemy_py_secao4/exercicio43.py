num1 = float(input("Insira o valor da compra: "))
value_discount = num1 * 0.90
instalments = num1 / 3
comis1 = value_discount * 0.05
comis2 = num1 * 0.05

print(f"O valor da compra a vista com desconto é {value_discount:.2f} \n"
      f"O valor de cada parcela é {instalments:.2f} \n"
      f"O valor da comissão em vendas a vista é {comis1:.2f} \n"
      f"O valor da comissão em vendas parceladas é {comis2:.2f} \n")
