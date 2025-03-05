try:
    numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

    result = numbers[0] - sum(numbers[1:])
    print("Result:", result)

except ValueError:
    print("Please enter valid integers.")
