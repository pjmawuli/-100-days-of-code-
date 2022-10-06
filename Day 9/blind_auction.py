# Calculator

# Add
def add(n1, n2):
    return n1 + n2

<<<<<<< HEAD

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
=======
running = True

persons_list = []


def list_people(bidder_name, bid_amount):
    person_dictionary = {"name": bidder_name, "bid": bid_amount}

    persons_list.append(person_dictionary)


while running:
    print(art.logo)
    print("Welcome to the Secret Auction Program ")

    name = input("What's your name? ")
    bid = int(input("How much are you willing to bid? "))

    list_people(name, bid)

    response = input("Would anyone else like to bid? ")
    if response == "no":
        running = False
    else:
        clearpy.clear()

highest_bid = persons_list[0]["bid"]
highest_bidder = persons_list[0]

for person in persons_list:

    if person["bid"] >= highest_bid:
        highest_bid = person["bid"]
        highest_bidder = person

highest_bidder_name = highest_bidder["name"]
highest_bidder_bid = highest_bidder["bid"]

print(f"Looks like {highest_bidder_name} with a bid of {highest_bidder_bid} has won the auction.")
>>>>>>> ae3bd11cce991d70a09802376b208d8fb2ae522d
