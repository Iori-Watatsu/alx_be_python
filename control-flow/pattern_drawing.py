number = int(input("Enter the size of pattern: "))

row = 0 

while row < number:
    
    for j in range(number):
        print("*", end="")

    print()
    row += 1