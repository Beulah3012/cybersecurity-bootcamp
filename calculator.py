# Part 1: Choose your numbers
number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

# Part 2: Choose your operation
operation = input("Enter your operation (+, -, *, /): ")

# Part 3: Perform the operation
if operation == "+":
    print("Result:", number1 + number2)

elif operation == "-":
    print("Result:", number1 - number2)

elif operation == "*":
    print("Result:", number1 * number2)

elif operation == "/":
    if number2 == 0:
        print("Operation is invalid: division by zero is not allowed.")
    else:
        print("Result:", number1 / number2)

