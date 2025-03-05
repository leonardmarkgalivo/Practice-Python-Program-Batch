try:
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    difference = num1 - num2
    print("The difference of two numbers is:", difference)

except ValueError:
    print("Please enter a valid number!")