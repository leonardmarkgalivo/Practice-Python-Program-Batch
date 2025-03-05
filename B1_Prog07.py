try:
    total = 0

    for i in range (10):
        num = float(input(f"Enter number {i+1}: "))
        total += num

    print("The sum of total numbers is: ", total)

except ValueError:
    print("Please enter a valid number!")