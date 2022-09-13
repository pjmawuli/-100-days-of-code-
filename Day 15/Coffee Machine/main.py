import app_data

money = 0


# Create a function that takes the coffee the user wants and subtracts the resources used from the available resource
def brew(coffee_type):
    app_data.resources["water"] -= app_data.MENU[coffee_type]["ingredients"]["water"]
    app_data.resources["milk"] -= app_data.MENU[coffee_type]["ingredients"]["milk"]
    app_data.resources["coffee"] -= app_data.MENU[coffee_type]["ingredients"]["coffee"]


while True:
    response = input("What would you like? (espresso/latte/cappuccino) ")
    if response == "report":
        print(
            f"Water: {app_data.resources['water']}ml \nMilk: {app_data.resources['milk']}ml \nCoffee: {app_data.resources['coffee']}g \nMoney: {money}$")
    if response == "espresso":
        brew(response)
