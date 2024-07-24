num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operator(*, +, -, /): ")

match operator: 
    case "+":
        result = num1 + num2 
        print(f"The result is: {result}")
    case "-":
        result = num1 - num2 
        print(f"The result is: {result} ")
    case "*": 
        result = num1 * num2 
        print(f"The result is: {result}")
    case "/":
        if num2 == 0:
            print("Error: Division by 0 is not allowed")
        else:
            result = num1 / num2 
            print(f"The result is: {result}")
    case _:
        print("invalid operator")