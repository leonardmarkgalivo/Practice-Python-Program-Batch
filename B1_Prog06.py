try:
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    result = num1 ** num2
    print(num1, "raised to the power of", num2, "is", result)

except ValueError:
    print("Please enter a valid number!")