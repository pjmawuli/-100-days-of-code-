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


def operate(first_num, second_num, operator):
    return operations[operator](first_num, second_num)


answer = operate(num1, num2, operation_symbol)

print(f"{num1} {operation_symbol} {num2} = {answer}")
