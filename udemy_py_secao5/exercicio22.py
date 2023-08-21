idade = int(input("Insert your age: "))
servico = int(input("Insert your time of labor: "))

if idade > 65 or servico >= 30:
    print("You are approved for retirement!")
elif idade > 60 and servico >= 25:
    print("You are approved for retirement!")
else:
    print("Your not approved for retirement!")

