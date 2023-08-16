num1 = float(input("Insert the value: "))
desc1 = num1 - (12/100)*100
print(f"The descount is {desc1}")

'''
Código esta errado por dificuldades matematicas. ele esta calculando o valor inserido menos 12,
e não menos 12%. Para calcular o desconto, deve-se usar a seguinte formula:

value = float(input("Insert the value: "))
discounted_value = value * (1 - 0.12)
print(f"The discounted value is {discounted_value:.2f}")

'''