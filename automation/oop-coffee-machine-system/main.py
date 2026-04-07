from menu import *
from money_machine import *
from coffee_maker import *

menu = Menu()
coffee_machine = CoffeeMaker()
coffee_machine_money = MoneyMachine()

ended = False
while not ended:
    user_input = input(f"What would you like?:{menu.get_items()}").lower()
    if user_input == "off":
        ended = True
        pass
    elif user_input == "report":
        print("here is your report:")
        coffee_machine.report()
        coffee_machine_money.report()
        pass
    else:
        drink = menu.find_drink(user_input)
        enough_resources = coffee_machine.is_resource_sufficient(drink)
        if enough_resources:
            print(f"Perfect, the total is: ${drink.cost}")
            coffee_machine_money.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)















