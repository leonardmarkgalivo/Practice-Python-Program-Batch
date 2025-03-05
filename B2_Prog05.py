try:
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    remainder = num1 % num2
    print("The remainder is: ", remainder)

except ValueError:
    print("Please enter a valid number!")