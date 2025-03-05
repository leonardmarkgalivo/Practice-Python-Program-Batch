try:
    num1 = float(input("First NUmber: "))
    num2 = float(input("Second NUmber: "))

    if num1 == num2:
        print("Equal")
    else:
        print("Not Equal")
except ValueError:
    print("Please enter a valid number!")

