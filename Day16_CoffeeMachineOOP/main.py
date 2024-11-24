from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def run_coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            coffee = menu.find_drink(choice)
            if coffee:
                if coffee_maker.is_resource_sufficient(coffee):
                    if money_machine.make_payment(coffee.cost):
                        coffee_maker.make_coffee(coffee)


if __name__ == "__main__":
    run_coffee_machine()