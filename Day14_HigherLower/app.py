from art import logo, vs
from data import data
import random

def higher_lower():
    compare_a = {}
    compare_b = {}
    score = 0

    while True:
        print(logo)

        if compare_a == {}:
            compare_a = select_data()
        else:
            print(f"You're right! Current score: {score}.")

        compare_b = select_data()
        winner = get_winner(compare_a, compare_b)

        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
        print(vs)
        print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if choice == winner:
            score += 1
            compare_a = compare_b
        else:
            break
        
        print("\n" * 20)

    print(f"Sorry, that's wrong. Final score: {score}")


def select_data():
    return random.choice(data)


def get_winner(a: dict, b: dict):
    if a['follower_count'] > b['follower_count']:
        return "a"
    else:
        return "b"


if __name__ == "__main__":
    higher_lower()