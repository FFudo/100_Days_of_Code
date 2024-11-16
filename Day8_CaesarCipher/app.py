from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encoded_text = ""
    for letter in original_text:
        shifted_pos = alphabet.index(letter) + shift_amount
        shifted_pos %= len(alphabet)
        encoded_text += alphabet[shifted_pos]

    print(encoded_text)

def decrypt(original_text, shift_amount):
    decoded_text = ""
    for letter in original_text:
        shifted_pos = alphabet.index(letter) - shift_amount
        shifted_pos %= len(alphabet)
        decoded_text += alphabet[shifted_pos]
    
    print(decoded_text)

decrypt(original_text=text, shift_amount=shift)