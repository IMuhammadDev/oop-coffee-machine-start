from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
payment = MoneyMachine()
mn = Menu()

print("Welcome to the coffee machine")

condition = True
while condition:
    options = mn.get_items()
    ask = input(f"what would you like {options}")
    if ask == "off":
        condition = False
    elif ask == "report":
        maker.report()
        payment.report()
    else:
        drink = mn.find_drink(ask)
        if payment.make_payment(drink.cost) and maker.is_resource_sufficient(drink):
            maker.make_coffee(drink)
