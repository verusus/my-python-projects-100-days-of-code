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


# todo: 4.1. a function that checks sufficiency depending on which drink chosen
def is_sufficient_for(name_of_drink):
    """checks if the resources are sufficient to make the drink or not and return true or false."""
    drink = MENU[name_of_drink]["ingredients"]
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]
    if name_of_drink == "espresso":
        return water >= drink["water"] and coffee >= drink["coffee"]
    else:
        return water >= drink["water"] and coffee >= drink["coffee"] and milk >= drink["milk"]


# todo 5.1: function that returns the change
def change(drink_name, n_quarters, n_dimes, n_nickels, n_pennies):
    drink_cost = MENU[drink_name]["cost"]
    user_money = 0.25 * n_quarters + n_dimes * 0.1 + n_nickels * 0.05 + n_pennies * 0.01
    return round(user_money - drink_cost, 2)


# todo: 7.1. a function that deduct from the resources once transation is done.
def deduct(drink_name, resources_list):
    """depending on the type of drink, it deducts requirements from the resources."""
    drink = MENU[drink_name]["ingredients"]

    resources_list["water"] -= drink["water"]
    resources_list["coffee"] -= drink["coffee"]
    if drink_name == "latte" or drink_name == "cappuccino":
        resources_list["milk"] -= drink["milk"]


# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
profit = 0
machine_on = True
while machine_on:
    request = input("  What would you like? (espresso/latte/cappuccino):").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if request == "off":
        machine_on = False

    # TODO: 4. Check resources if sufficient?
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        if not is_sufficient_for(request):
            print("Sorry there is not enough water.")
        else:
            # TODO: 5. Process coins.
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            change_value = change(request, quarters, dimes, nickels, pennies)
            if change_value < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                cost = MENU[request]["cost"]
                profit += cost
                print(f"Here is ${change_value} dollars in change.")
                # TODO: 7. Make Coffee.
                deduct(request, resources)
                print(f"Here is your {request} ☕. Enjoy!")

    # TODO: 3. Print report.
    # # TODO: 3.1. track the machine money
    elif request == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: {profit}")

