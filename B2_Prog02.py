try:
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    if num1 != num2:
        print("Not Equal")
    else:
        print("Equal")

except ValueError:
    print("Please enter a valid number!")