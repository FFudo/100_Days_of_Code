from data import resources, MENU

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()

        if choice == "off":
            break
        elif choice == "report":
            print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}")
        else:
            bev = MENU[choice]
            status = check_resources(bev["ingredients"])
            if status != "full":
                print(f"Sorry we there is not enough {status}")
        

def check_resources(ingredients: dict):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            return ingredient
        
    return "full"


if __name__ == "__main__":
    coffee_machine()