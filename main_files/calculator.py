import re
import sys

try:
    number = input("Enter a mathematical equation:  ").strip()
    if not re.search(r"^\d+\s[+\-*/]\s\d+$", number):
        print("Invalid format")
        sys.exit()
    
    first, condition, second = number.split(" ")
    first = int(first)
    second = int(second)

    if condition == "+":
        equation = first + second
    elif condition == "-":
        equation = first - second
    elif condition == "*":
        equation = first * second
    elif condition == "/" and second != 0:
        equation = first / second
    else:
        print("Invalid Operator or Division by Zero")
        sys.exit()

    print(equation)

except ValueError:
    print("Please enter the correct format")
