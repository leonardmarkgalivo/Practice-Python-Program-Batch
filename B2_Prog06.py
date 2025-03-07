first_num = int(input("Enter number 1: ")) 

result = first_num  

for i in range(2, 11):  
    num = int(input(f"Enter number {i}: "))
    result -= num  

print(f"Result: {result}")  
