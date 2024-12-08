import pandas as pd

df = pd.read_csv("./Day26_NatoAlphabet/nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}

while True:
    try:
        word = input("Enter a word: ").upper()
        output_list = [alphabet_dict[letter] for letter in word]
        break
    except:
        print("Sorry, only letters in the alphabet please.")

print(output_list)
