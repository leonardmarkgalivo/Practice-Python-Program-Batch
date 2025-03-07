try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    start = min(num1, num2)
    end = max(num1, num2)

    for num in range(start + 1, end):
        print(num, end=" ")  

except ValueError:
    print("Please enter valid integers.")

