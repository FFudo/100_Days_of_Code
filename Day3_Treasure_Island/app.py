print(r'''.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
.            _.,.__       .                                   .
.           ((o\\o\))     .                                   .
.     .-.    `  \\``      .    Welcome to Treasure            .
.  __(   )___.o"^^".,___  .             Island                .
.     ===    ~~~~~~~~     .                                   .
.      ==             ldb .                                   .
.       =                 .                                   .
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
''')

print("Welcome to Treasure Island. Your mission is to find the treasure")

choice = input("There is a path to your right and one to your left. Which do you choose? Type 'left' or 'right'.").lower()

if choice == "left":
    choice = input("There is a river in front of you the current looks strong. You can either cross it or look for a better way. Type 'cross' or 'search'").lower()
    if choice == "search":
        choice = input("You found a bridge to cross. After some walking there is a house with a yellow, a blue or a green door. Choose one and type 'yellow', 'green' or 'blue'").lower()
        if choice == "blue":
            print("A vicious beast attacked you! Game Over.")
        elif choice == "green":
            print("You were engulfed by flames and burned to death. Game Over.")
        elif choice == "yellow":
            print("You found the treasure. Well Done!")
        else:
            print("Standing around, doing nothing, your body gave up. Game Over.")
    else:
        print("The current was too strong. You didn't make it. Game Over.")
else:
    print("A snake attacked you. Game Over.")
