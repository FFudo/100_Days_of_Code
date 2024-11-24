from data import resources, MENU

OPTIONS = ["off", "report", "espresso", "latte", "cappuccino"]

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()

        if choice not in OPTIONS:
            print("Please insert a valid value!")
            continue

        if choice == "off":
            break
        elif choice == "report":
            show_report()
        else:
            bev = MENU[choice]
            status = check_resources(bev["ingredients"])
            if status != "full":
                print(f"Sorry there is not enough {status}")
                continue
            money = get_coins()
            if not is_enough_money(money, bev["cost"]):
                continue
            update_report(bev["cost"])
            make_coffee(bev["ingredients"], choice)


def make_coffee(ingredients: dict, coffee: str):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {coffee}. Enjoy!")
    

def show_report():
     print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}")


def update_report(profit: float):
    resources["money"] += profit

            
def is_enough_money(customer_money: float, bev_cost: float):
    if customer_money >= bev_cost:
        if not customer_money == bev_cost:
            print(f"Here is ${round(customer_money - bev_cost, 2)} dollars in change")
        return True
    else:
        print("Sorry thats not enough money. Money refunded.")
        return False


def check_resources(ingredients: dict):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            return ingredient
        
    return "full"


def get_coins():
    print("Please insert coins.")
    quarters = int(input("Hopw many quarters?:"))
    dimes = int(input("Hopw many dimes?:"))
    nickles = int(input("Hopw many nickles?:"))
    pennies = int(input("Hopw many pennies?:"))
    return round((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01), 2)


if __name__ == "__main__":
    coffee_machine()