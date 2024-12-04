import pandas as pd

df = pd.read_csv("./Day26_NatoAlphabet/nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ")

letters = [letter.upper() for letter in word]

print([alphabet_dict[letter] for letter in letters])
