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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




# TODO: 1. Print report of all coffee achine resources

def report(resources, money):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")

# TODO: 2. Check reosurces sufficient?

def check_resources(resources, menu):
    water_need = menu["ingredients"]["water"]
    milk_need = menu["ingredients"].get("milk", 0)
    coffee_need = menu["ingredients"]["coffee"]
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if water_need > water or milk_need > milk or coffee_need > coffee:
        print("Sorry, not enough materials for that")
        return False
    else:
        return True

# TODO: 3. Process coins

def coins(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters * 0.25
    total += dimes * 0.10
    total += nickels * 0.05
    total += pennies * 0.01
    return total
    
# TODO: 4. Check transaction successful

def transaction(user_money, cost):
    if user_money - cost < 0:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here's ${user_money - cost} in change")
        return True

# TODO: 5. Make Coffee

def complete_ops(resources, cost):
    resources["water"] -= cost["ingredients"]["water"]
    resources["milk"] -= cost["ingredients"].get("milk", 0)
    resources["coffee"] -= cost["ingredients"]["coffee"]
    return

on = True
while on == True:
    user_choice = input("What would you like? (espresso/latte/cappuccino):  ")
    if user_choice == "report":
        report(resources, profit)
    elif user_choice == "off":
        on = False
    else:
        user_choice_cost = MENU[user_choice]["cost"]
        user_choice_drink = MENU[user_choice]
        print("Please insert coins.")
        quartes = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        resources_ok = check_resources(resources, user_choice_drink)
        if resources_ok == True:
            inserted_coins = coins(quartes, dimes, nickles, pennies)
            transaction_ok = transaction(inserted_coins, user_choice_cost)
            if transaction_ok == True:
                complete_ops(resources, user_choice_drink)
                profit += user_choice_cost
                print(f"Here's your {user_choice}. Enjoy!")


