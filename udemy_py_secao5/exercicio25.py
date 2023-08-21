import math
a = int(input("Insert the coefficient A: "))
b = int(input("Insert the coefficient B: "))
c = int(input("Insert the coefficient C: "))

if a > 0:
    delt = b**2 - 4*a*c
    if delt < 0:
        print("Square root doesn't exist! ")
    elif delt == 0:
        print("Unique square root!")
    else:
        x1 = (-b + math.sqrt(delt)) / (2 * a)
        x2 = (-b - math.sqrt(delt)) / (2 * a)
        print(f"The square root for the equation {a}x² + {b}x + {c} is x1 = {x1} and x2 = {x2}")
else:
    print("It's not a second degree equation!")

'''
chat gpt correction with comments (in portuguese)
The main error was the non use of parenthesis, which is necessary if we are going to receive negative numbers
in the calculus.

import math

# Input coefficients from the user
a = int(input("Insert the coefficient A: "))
b = int(input("Insert the coefficient B: "))
c = int(input("Insert the coefficient C: "))

# Check if it's a second-degree equation (a != 0)
if a != 0:
    # Calculate the discriminant
    delt = b**2 - 4*a*c

    # Check if the roots are complex numbers
    if delt < 0:
        print("Square roots are complex numbers.")
    # If the discriminant is zero, there's a single real root
    elif delt == 0:
        x1 = -b / (2 * a)
        print(f"Unique root: x = {x1}")
    # If the discriminant is positive, there are two real roots
    else:
        x1 = (-b + math.sqrt(delt)) / (2 * a)
        x2 = (-b - math.sqrt(delt)) / (2 * a)
        print(f"The roots are x1 = {x1} and x2 = {x2}")
else:
    print("It's not a second-degree equation!")

'''
