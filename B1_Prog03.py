try:
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    sum = num1 + num2
    print("The sum of two numbers is: ", sum)

except ValueError:
    print("Please enter a valid number!")