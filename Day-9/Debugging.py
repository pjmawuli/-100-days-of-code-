# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("Enter the first number: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("Enter the second number: "))

calculator_function = operations[operation_symbol]
num3 = calculator_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {num3}")

operation_symbol = input("Pick another operation from above: ")
num4 = int(input("What's the number: "))
calculator_function = operations[operation_symbol]
num5 = calculator_function(num4, num3)

print(f"{num3} {operation_symbol} {num4} = {num5}")