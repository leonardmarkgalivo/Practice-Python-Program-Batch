try:
    num1 = float(input("First Number: "))
    num2 = float(input("Second NUmber:"))

    quotient = num1 / num2
    print("The quotient of two numbers is: ", quotient)

except ValueError:
    print("Please enter a valid number!")

