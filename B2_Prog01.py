try:
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    if num1 > num2:
        print("The smallest number is", num2)
    elif num1 < num2:
        print("The smallest number is", num1)
    else:
        print("Both are equal")

except ValueError:
    print("Please enter a valid number!")
