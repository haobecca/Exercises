import string

def is_pangram(sentence):
    sentence = sentence.strip(string.punctuation + string.digits).lower()
    letter_check = list(string.ascii_lowercase)
    for letter in sentence:
        if letter in letter_check:
            letter_check.remove(letter)
    return letter_check == []
