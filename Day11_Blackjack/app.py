from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    loop = True
    while loop:
        print(logo)
        player_hand = []
        comp_hand = []
        deal_cards(player_hand, 2)
        deal_cards(comp_hand, 2)

        print_status(player_hand, comp_hand)

        repeat = input("Type 'y' to get another card, type 'n' to pass:").lower()

        while repeat == "y":
            deal_cards(player_hand, 1)
            player_hand = check_ace(player_hand)

            if sum(player_hand) > 21:
                break

            print_status(player_hand, comp_hand)
            repeat = input("   Type 'y' to get another card, type 'n' to pass:").lower()
        
        while sum(comp_hand) < 17 and sum(player_hand) <= 21:
            deal_cards(comp_hand, 1)
            comp_hand = check_ace(comp_hand)

        display_winner(player_hand, comp_hand)

        again = input("Do you want to play again? Type 'y' or 'no'.").lower()

        if again == "n":
            loop = False


def deal_cards(hand: list, card_number: int):
    for n in range(card_number):
        hand.append(random.choice(cards))


def print_status(p_hand: list, c_hand: list):
    print(f"    Your cards: {p_hand}, current score: {sum(p_hand)}")
    print(f"    Computers first card: {c_hand[0]}")


def display_winner(p_hand: list, c_hand: list):
    c_score = sum(c_hand)
    p_score = sum(p_hand)
    print(f"    Your cards: {p_hand}, final score: {p_score}")
    print(f"    Computer cards: {c_hand}, final score: {c_score}")
    if p_score > 21:
        print(  "You are over 21. You lose!")
    elif c_score > 21:
        print("Computer is over 21. You won!")
    elif p_score > c_score:
        print("You won! Good job!")
    elif p_score == c_score:
        print("Draw!")
    else:
        print("You lost...")


def check_ace(hand: list):
    if 11 in hand:
        if sum(hand) > 21:
            index = hand.index(11)
            hand[index] = 1
    return hand


if __name__ == "__main__":
    blackjack()