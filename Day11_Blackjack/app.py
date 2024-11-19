from art import logo
import random
# TODO implement winning logic
# TODO impplement over 21 logic
# TODO implement ace 1 or 11 logic
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

            if sum(player_hand) > 21:
                break

            print_status(player_hand, comp_hand)
            repeat = input("   Type 'y' to get another card, type 'n' to pass:").lower()
        
        while sum(comp_hand) < 17:
            deal_cards(comp_hand, 1)

        display_winner(player_hand, comp_hand)

        again = input("Do you want to play again? Type 'y' or 'no'.").lower()

        if again == "n":
            loop = False


def deal_cards(hand: list, card_number: int):
    for n in range(card_number):
        hand.append(random.choice(cards))


def print_status(p_hand, c_hand):
    print(f"    Your cards: {p_hand}, current score: {sum(p_hand)}")
    print(f"    Computers first card: {c_hand[0]}")


def display_winner(p_hand, c_hand):
    c_score = sum(c_hand)
    p_score = sum(p_hand)
    print(f"    Your cards: {p_hand}, final score: {p_score}")
    print(f"    Computer cards: {c_hand}, final score: {c_score}")
    if p_score > c_score:
        print(  "You win! Good Job!")

if __name__ == "__main__":
    blackjack()