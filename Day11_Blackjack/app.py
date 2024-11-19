from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
comp_hand = []

for n in range(2):
    player_hand.append(random.choice(cards))
    comp_hand.append(random.choice(cards))


print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
print(f"Computers first card: {comp_hand[0]}")

repeat = input("Type 'y' to get another card, type 'n' to pass:").lower()


