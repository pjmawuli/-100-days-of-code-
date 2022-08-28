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


def calculator():
    active = True

    num1 = int(input("Enter the first number: "))

    while active:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = int(input("Enter another number: "))

        calculator_function = operations[operation_symbol]
        num3 = calculator_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {num3}")
        num1 = num3

        response = input(f"Type 'y' to continue using the previous result and 'n' to start over: ")
        if response == 'n':
            active = False
            calculator()


calculator()
