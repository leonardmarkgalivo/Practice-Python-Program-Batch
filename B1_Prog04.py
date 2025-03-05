try:
    num1 = float(input("First Number: "))
    num2 = float(input("Second NUmber "))

    product = num1 * num2
    print("The product of two numbers is: ", product)

except ValueError:
    print("Please enter a valid number!")