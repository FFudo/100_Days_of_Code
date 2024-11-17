from art import logo

print(logo)
print("Welcome to the secret auction program.")

loop = True
all_bids = {}

while loop:
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    all_bids[name] = bid

    if other_bidders == "no":
        loop = False

    print("\n" * 20)

winner_bid = 0
winner_name = ""

for key in all_bids:
    if all_bids[key] > winner_bid:
        winner_bid = all_bids[key]
        winner_name = key

print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
