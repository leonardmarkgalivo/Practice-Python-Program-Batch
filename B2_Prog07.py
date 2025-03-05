try:
    numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

    even_count = sum(1 for num in numbers if num % 2 == 0)
    print("Count of even numbers:", even_count)

except ValueError:
    print("Please enter valid integers.")
