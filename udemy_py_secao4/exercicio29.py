num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
num3 = int(input("Input the third number: "))
num4 = int(input("Input the fourth number: "))

media = (num1 + num2 + num3 + num4) / 4
print("The average is:", str(media))

'''
Versão do Chat gpt:

num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
num3 = int(input("Input the third number: "))
num4 = int(input("Input the fourth number: "))

numbers = [num1, num2, num3, num4]
media = sum(numbers) / len(numbers)

print("The average is:", media)

In this improved version, we create a list numbers containing all the input numbers.
Then, we use the sum() function to calculate the sum of the elements in the numbers list, and we divide it by the number of elements in the list (in this case, 4) to get the average.
By using the sum() function and a list, the code becomes more scalable and easier to maintain.
If you need to calculate the average of more numbers in the future, you can simply add them to the numbers list without modifying the calculation logic.
'''