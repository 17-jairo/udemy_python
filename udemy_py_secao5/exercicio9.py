num1 = float(input("Insert your salary: "))
num2 = float(input("Insert your financing payment: "))

if num2 > (0.2 * num1):
    print("Financing not granted!")
else:
    print("Financing granted.")
