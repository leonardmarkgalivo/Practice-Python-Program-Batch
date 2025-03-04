try:
    num1 = float(input("First Number:"))
    num2 = float(input("Second Number: "))

    if num1 > num2:
        print("The bigger number is: ", num1)
    elif num1 < num2:
        print("The bigger number is: ", num2)
    else:
        print("Both are Equal")

except ValueError:
    print("Please enter a valid number!")