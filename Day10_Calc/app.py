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

number1 = float(input("Whats the first number?: "))

for key in calculations:
    print(key)

operator = input("Pick an operation: ")
number2 = float(input("Whats the next number? "))

result = calculations[operator](number1, number2)

print(f"{number1} {operator} {number2} = {result}")
