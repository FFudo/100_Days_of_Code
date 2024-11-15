import hangman_art
import hangman_words
import random

lives = len(hangman_art.stages) - 1
game_over = False

secret_word = random.choice(hangman_words.word_list)

placeholder = ""
correct_chars = []

for char in secret_word:
    placeholder += "_"

print(hangman_art.logo)

while not game_over:
    print(secret_word)
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    print(f"Word to gues: {placeholder}")
    guess = input("Guess a letter: ").lower()

    if guess in correct_chars:
        print(f"You have already guessed: {guess}")

    display = ""

    for char in secret_word:
        if char == guess:
            display += guess
            correct_chars.append(guess)
        elif char in correct_chars:
            display += char
        else:
            display += "_"
    
    placeholder = display

    if guess not in secret_word:
        lives -=1
        print(f"Sorry your guess {guess} is not in the word. You lose a life.")
    else:
        print(f"Correct! {guess} is in the word.")
    
    print(hangman_art.stages[lives])

    if lives == 0:
        game_over = True
        print(f"You lost. The correct word was: {secret_word}")
    elif "_" not in placeholder:
        game_over = True
        print(f"You won.")