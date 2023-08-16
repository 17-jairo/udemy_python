num1 = int(input("Entrez le numero: "))
cal1 = num1 - 1
cal2 = num1 + 1
print("Votre numero précedent est " + str(cal1) + " est votre numero suivant est " + str(cal2))

'''
O chat gpt sugeriu o uso de f-strings nesse caso, para deixar o código mais claro de ler:

num1 = int(input("Enter the number: "))
previous = num1 - 1
next_num = num1 + 1
print(f"Your previous number is {previous} and your next number is {next_num}")

This allows you to directly insert the values of the variables into the string 
without explicitly converting the values to strings using str().
'''