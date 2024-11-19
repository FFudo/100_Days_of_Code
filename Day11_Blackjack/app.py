from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
comp_hand = []
loop = True


def blackjack():
    while loop:
        reset_hands()
        deal_cards(player_hand, 2)
        deal_cards(comp_hand, 2)

        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"Computers first card: {comp_hand[0]}")

        repeat = input("Type 'y' to get another card, type 'n' to pass:").lower()


def reset_hands():
    player_hand = []
    comp_hand = []


def deal_cards(hand: list, card_number: int):
    for n in range(card_number):
        hand.append(random.choice(cards))


if __name__ == "__main__":
    blackjack()