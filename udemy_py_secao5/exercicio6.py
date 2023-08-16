num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if num1 > num2:
    sub = num1 - num2
    print(f'O maior numero é {num1} e a diferença entre eles é {sub}.')
else:
    sub2 = num2 - num1
    print(f"O maior número é {num2} e a diferença entre eles é {sub2}.")
