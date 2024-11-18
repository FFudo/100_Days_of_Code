from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calculations = {"+": add,
                "-": subtract,
                "*": multiply,
                "/": divide,
                }

print(logo)

loop = True
while loop:
    number1 = float(input("Whats the first number?: "))
    continue_with_n1 = True

    while continue_with_n1:
        for key in calculations:
            print(key)

        operator = input("Pick an operation: ")
        number2 = float(input("Whats the next number? "))

        result = calculations[operator](number1, number2)

        print(f"{number1} {operator} {number2} = {result}")
        user_choice = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or 'q' to quit the programm.").lower()

        if user_choice != "y":
            continue_with_n1 = False
            if user_choice == "q":
                loop = False

        number1 = result
