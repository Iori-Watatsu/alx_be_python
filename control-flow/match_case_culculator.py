num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case result if num1 + num2:
        print(f"The result is {result} .") 
