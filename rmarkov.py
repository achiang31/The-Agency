import os
import string

def markovchain():
    alphabet = dict.fromkeys(string.ascii_lowercase,
    dict.fromkeys(string.ascii_lowercase, 0))
    with open("./corpora/corpora.txt", encoding = "utf-16") as f:
        all_text = f.read().encode("ascii", "ignore")
    all_text = all_text.lower()
    last = all_text[0]
    all_text[1:]
    for character in all_text:
        try:
            alphabet[last][character] += 1
            last = character
        except KeyError:
            last = character
    f.close()
    print(alphabet)

markovchain()