import random, sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
comp_choice = random.randint(0,2)

print("Welcome to Rock, Paper, Scisscor!")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if choice > 2 or  choice < 0:
    print("You typed an invalid number. You lose!")
    sys.exit()

print(f"Your choice : \n{options[choice]}")
print(f"Computer chose: \n {options[comp_choice]}")


if choice == 0 and comp_choice == 2:
    print("You win!")
elif choice == 2 and comp_choice == 0:
    print("You lose!")
elif choice > comp_choice:
    print("You win!")
elif comp_choice > choice:
    print("You lose!")
else:
    print("Draw!")
