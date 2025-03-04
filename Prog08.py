try:
    odd_count = 0

    for i in range (10):
        num = float(input(f"Enter number {i+1}: "))

        if num % 2 != 0:
            odd_count += 1

    print("The number of odd numbers is:", odd_count)

except ValueError:
    print("Please enter a valid number!")