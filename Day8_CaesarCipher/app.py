from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode, original_text, shift_amount):
    if encode_or_decode == "decode":
        shift_amount *= -1

    output_text = ""

    for letter in original_text:
        if letter in alphabet:
            shifted_pos = alphabet.index(letter) + shift_amount
            shifted_pos %= len(alphabet)
            output_text += alphabet[shifted_pos]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")

is_looping = True

while is_looping:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()

    if restart == "no":
        is_looping = False
        print("Goodbye")