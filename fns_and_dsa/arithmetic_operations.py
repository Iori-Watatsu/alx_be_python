def perform_operation(num1, num2, operation):
    print("Arithmetic Operations")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Enter the operation (add, subtract, multiply, divide): ")
    match operation:
        case "add":
            result = num1 + num2
            print("Result: ", result)
        case "subtract":
            result = num1 - num2
            print("Result: ", result)
        case "multiply":
            result = num1 * num2
            print("Result: ", result)
        case "divide":
            if num1 == 0:
                print("Cannot divide by 0.")
            else:
                result = num1 / num2
                print("Result: ", result)
    return result
perform_operation()