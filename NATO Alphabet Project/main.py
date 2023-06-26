import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

df = pandas.DataFrame(data)

nato_dict = {
    row.letter: row.code for (index, row) in data.iterrows()
}

word = str(input("Enter a word: ")).upper()
phonetic = [nato_dict[letter] for letter in word]

print(phonetic)

