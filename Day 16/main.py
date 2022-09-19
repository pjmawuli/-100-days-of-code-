from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee():
    menu = Menu()
    coffee_machine = CoffeeMaker()
    counter = MoneyMachine()

    while True:

        response = input(f"What would you like? ({menu.get_items()}) ")

        if response == "off":
            print(f"The program is closing.")
            break

        if response == "report":
            coffee_machine.report()
            counter.report()

        if response == "espresso":
            drink = menu.find_drink("espresso")
            if coffee_machine.is_resource_sufficient(drink):
                if counter.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)

        if response == "latte":
            drink = menu.find_drink("latte")
            if coffee_machine.is_resource_sufficient(drink):
                if counter.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)

        if response == "cappuccino":
            drink = menu.find_drink("cappuccino")
            if coffee_machine.is_resource_sufficient(drink):
                if counter.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)


coffee()
