nota = float(input("Insert your score: "))
faltas = int(input("Insert the absences: "))

if 9.0 <= nota <= 10.0:
    if faltas < 20:
        print("Seu conceito é A")
    else:
        print("Seu conceito é B.")
elif 7.5 <= nota <= 8.9:
    if faltas < 20:
        print("Seu conceito é B")
    else:
        print("Seu conceito é C.")
elif 5.0 <= nota <= 7.4:
    if faltas < 20:
        print("Seu conceito é C")
    else:
        print("Seu conceito é D.")
elif 4.0 <= nota <= 4.9:
    if faltas < 20:
        print("Seu conceito é D")
    else:
        print("Seu conceito é E.")
elif 0.0 <= nota <= 4.9:
    if faltas < 20:
        print("Seu conceito é E")
    else:
        print("Seu conceito é E.")
else:
    print("Numero invalido!")

