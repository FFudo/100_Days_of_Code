from art import logo
import random

SECRET_NUMBER = random.randint(1, 100)

def guessing_game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    play_game(difficulty)


def play_game(dif):
    if dif == 'hard':
        attempts = 5
    else:
        attempts = 10

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))

        if guess == SECRET_NUMBER:
            print(f"You got it! The answer was {SECRET_NUMBER}.")
            break
        elif guess > SECRET_NUMBER:
            print("Too high.")
        else:
            print("Too low.")

        print("Guess again!")
        attempts -= 1
    
    if attempts == 0:
        print(f"You have no attempts left! The answer was {SECRET_NUMBER}.")


if __name__ == "__main__":
    guessing_game()