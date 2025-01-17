from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
avaible_items = Menu()


on = True
while on == True:
    user_choice = input(f"What would you like? ({avaible_items.get_items()}):  ")
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        on = False
    else:
        search_request = avaible_items.find_drink(user_choice)
        if search_request == None:
            print(f"There is no {search_request}, please make a valid selection")
        else:
            if coffee_maker.is_resource_sufficient(search_request) == True:
                if money_machine.make_payment(search_request.cost) == True:
                    coffee_maker.make_coffee(search_request)