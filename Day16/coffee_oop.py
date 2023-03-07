from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_machine_on = True

while is_machine_on:

    coffee_choices = menu.get_items()
    ask_customer = input(f"What would you like: {coffee_choices} ")

    if ask_customer == 'off':
        is_machine_on = False
        print("Bye")
    elif ask_customer == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        customer_choice_drink = menu.find_drink(ask_customer)
        if coffee_maker.is_resource_sufficient(customer_choice_drink) and money_machine.make_payment(customer_choice_drink.cost):
            coffee_maker.make_coffee(customer_choice_drink)

