MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 5. Create a american coins for purchase the latte
coins = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickle": 0.05,
    "pennies": 0.01,
}

profit = 0

def report(total_money):
    """Check the resources available"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${total_money}")

def enough_resources(order_ingredients):
    """Check if drink can be made out of the left resources"""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def calculate_coins():
    print("Please insert coins.")
    total_coins = int(input("How many quarters?: ")) * coins["quarter"]
    total_coins += int(input("How many dimes?: ")) * coins["dime"]
    total_coins += int(input("How many nickles?: ")) * coins["nickle"]
    total_coins += int(input("How many pennies?: ")) * coins["pennies"]
    return total_coins

    # TODO: 6: Check if coins given is enough, give change if coins is too much
def is_payment_success(payment, drink_cost):
    total_change = payment - drink_cost
    total_change = round(total_change, 2)
    if total_change <= 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        print(f"Here is ${total_change} in change.")
        return True

def make_drink(drink, order_ingredient):
    """Deduct the resources if the drink is make"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink}. Enjoy!")

# TODO: 1. Prompt to order the drink

def coffee_machine():
    machine_on = True
    while machine_on:
        order = input("\nWhat would you like? (espresso/latte/cappuccino):").lower()

        # TODO: 2. Turn off the coffee machine
        if order == "off":
            machine_on = False

        # TODO: 3. Create a inventory report of water, milk, coffee and money
        elif order == "report":
            report(profit)

        # TODO: 4. Check if the resources is enough water, milk and coffee
        elif order == "espresso" or "latte" or "cappuccino":
            #drink_order = MENU[order]
            got_resources = enough_resources(MENU[order]["ingredients"])
            if got_resources:
                payment = calculate_coins()
                if is_payment_success(payment, MENU[order]["cost"]):
                    make_drink(order, MENU[order]["ingredients"])

coffee_machine()