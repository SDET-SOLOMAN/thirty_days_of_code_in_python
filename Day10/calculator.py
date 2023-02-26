from my_art.calculator_app import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def my_operation(operation_name='/'):
    """This is calc operation"""

    my_dict = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    return my_dict[operation_name]


def calculator():
    print(logo)

    calculating = True

    num1 = round(float(input("Whats the first number? ")), 4)

    my_dict = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    while calculating:

        for k, v in my_dict.items():
            print(k)

        operation_symbol = input("Pick an operation from the line above? ")

        num2 = round(float(input('Whats the next number? ')), 4)

        answer = my_operation(operation_symbol)(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_answer = input('Do you want to keep calculating? y/n? ')

        if user_answer == 'y':
            num1 = answer
        else:
            calculating = False
            print("\n" * 20)
            calculator()


calculator()
