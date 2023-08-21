import math

inse1 = str(input("Escolha uma das operações abaixo: \n a - Geométrica \n b - Ponderada "
                  "\n c - Harmônica \n d - Aritmética \n Insira sua operação (a, b, c ou d): "))
inse2 = str.upper(inse1)
num1 = int(input("Insira o X: "))
num2 = int(input('Insira o Y: '))
num3 = int(input('Insira o Z: '))
if num1 > 0 and num2 > 0 and num3 > 0:
    if inse2 == "A":
        geometrica = math.pow((num1 * num2 * num3), 1/3)
        print(f"O calculo geometrico é {geometrica:.2f}")
    elif inse2 == "B":
        ponderada = (num1 + (2 * num2) + (3 * num3)) / 6
        print(f"O calculo ponderado é {ponderada:.2f}")
    elif inse2 == "C":
        harmonica = 1 / ((1/num1) + (1/num2) + (1/num3)) #Correçao do chat gpt, importante
        # incluir os parenteses na operaçao como um so.
        print(f"O calculo harmonico é {harmonica:.2f}")
    elif inse2 == "D":
        aritmetico = (num1 + num2 + num3) / 3
        print(f"O valor aritmético é {aritmetico:.2f}")
    else:
        print("Favor inserir a operação escolhida conforme descrito no enunciado!")
else:
    print("Operação valida somente para números positivos!")

