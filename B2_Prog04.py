try:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))

    quotient = num1 // num2
    print("The quotient of two numbers:", quotient)

except ValueError:
    print("Please enter a valid number")