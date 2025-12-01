from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

def coffee_machine():
    machine_on = True
    while machine_on:
        options = menu.get_items()
        order = input(f"\nWhat would you like? {options}:").lower()
        if order == "off":
            machine_on = False

        elif order == "report":
            coffee_maker.report()
            money_machine.report()

        elif order == "espresso" or "latte" or "cappuccino":
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

coffee_machine()