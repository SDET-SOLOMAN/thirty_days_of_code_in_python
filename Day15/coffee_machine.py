from my_art.coffee_machine import logo, MENU, resources
from datetime import date


def what_would_you_like():
    return input("What would you like? (espresso, latte, cappuccino? )").lower()


def water_check(user_input):
    return MENU[user_input]["ingredients"].get('water')


def milk_check(user_input):
    if user_input == 'espresso':
        return 0
    else:
        return MENU[user_input]["ingredients"]['milk']


def coffee_check(user_input):
    return MENU[user_input]["ingredients"].get('coffee')


def report_for_owner(water, milk, coffee, money):
    print(f"Water: {water} ml")
    print(f"Milk: {milk} ml")
    print(f"Coffee: {coffee} g")
    print(f"Money: ${money} USD")
    today = date.today()
    return "Report generated on ", today


def money_counter(user_input):

    req_price = MENU[user_input]["cost"]
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0

    print("please insert your money")

    user_quarters = int(input("How many quarters?: "))
    quarters = user_quarters / 4
    user_dimes = int(input("How many dimes?: "))
    dimes = (user_dimes) / 10
    user_nickles = int(input("How many nickles?: "))
    nickles = user_nickles / 20
    user_pennies = int(input("How many pennies?: "))
    pennies = user_pennies / 100

    return round(abs(dimes + nickles + quarters + pennies), 2)


def coffee_machine():

    water = resources["water"]
    milk = resources['milk']
    coffee = resources['coffee']
    money = 0

    while True:

        a = what_would_you_like()

        if a == 'report':
            print(report_for_owner(water, milk, coffee, money))

        else:

            needed_water = water_check(a)
            needed_milk = milk_check(a)
            needed_coffee = coffee_check(a)

            if needed_water > water:
                print(f"Not Enough water")
            elif needed_milk > milk:
                print("Not enough milk")
            elif needed_coffee > coffee:
                print("Not enough coffee")
            else:

                water -= needed_water
                milk -= needed_milk
                coffee -= needed_coffee

                customer_money = money_counter(a)

                if customer_money < MENU[a]["cost"]:
                    print("Sorry that's not enough\nRefunded")
                else:
                    print(f"Here is your change {round(customer_money - MENU[a]['cost'],2)}")
                    print(f"Enjoy your coffee {logo}")
                    money += MENU[a]["cost"]


coffee_machine()
