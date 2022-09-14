import app_data


# Create a function that takes the coffee the user wants and subtracts the resources used from the available resource
def brew(coffee_type):
    app_data.resources["water"] -= app_data.MENU[coffee_type]["ingredients"]["water"]
    app_data.resources["milk"] -= app_data.MENU[coffee_type]["ingredients"]["milk"]
    app_data.resources["coffee"] -= app_data.MENU[coffee_type]["ingredients"]["coffee"]
    print(f"Here's your lovely cup of {coffee_type}")


# Create a function to check if the resources are sufficient to brew that coffee
def check(coffee_type):
    if app_data.resources["water"] > app_data.MENU[coffee_type]["ingredients"]["water"]:
        if app_data.resources["milk"] > app_data.MENU[coffee_type]["ingredients"]["milk"]:
            if app_data.resources["coffee"] > app_data.MENU[coffee_type]["ingredients"]["coffee"]:
                return True
    else:
        return False


# Create a function that accounts for the money spent
def amount(coffee_type):
    return app_data.MENU[coffee_type]["cost"]


# Create a function that asks the user to enter the amount of money he is going to pay
def pay(coffee_type):
    quarters = int(input("How many dimes are you paying? ")) * 0.25
    dimes = int(input("How many dimes are you paying? ")) * 0.1
    nickels = int(input("How many nickels are you paying? ")) * 0.05
    pennies = int(input("How many pennies are you paying? ")) * 0.01

    total_amount = quarters + dimes + nickels + pennies
    if total_amount > app_data.MENU[coffee_type]["cost"]:
        print(f"Your change is {round(total_amount - app_data.MENU[coffee_type]['cost'], 2)}")
        return True
    elif total_amount == app_data.MENU[coffee_type]["cost"]:
        return True
    else:
        print(
            f"Sorry a {coffee_type} costs ${app_data.MENU[coffee_type]['cost']}. Here's your money back: ${round(total_amount, 2)}")
        return False


def coffee_machine():
    money = 0
    while True:
        response = input("What would you like? (espresso/latte/cappuccino) ")
        if response == "report":
            print(
                f"Water: {app_data.resources['water']}ml \nMilk: {app_data.resources['milk']}ml \nCoffee: {app_data.resources['coffee']}g \nMoney: ${money}")
        if response == "espresso" or response == 1:
            if check(response):
                if pay(response):
                    brew(response)
                    money += amount(response)
            else:
                print("Sorry there isn't enough resources to brew your coffee")

        if response == "latte" or response == 2:
            if check(response):
                if pay(response):
                    brew(response)
                    money += amount(response)
            else:
                print("Sorry there isn't enough resources to brew your coffee")
        if response == "cappuccino" or response == 3:
            if check(response):
                if pay(response):
                    brew(response)
                    money += amount(response)
            else:
                print("Sorry there isn't enough resources to brew your coffee")
        if response == "off":
            break


coffee_machine()
