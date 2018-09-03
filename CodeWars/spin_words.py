'''
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed
(Just like the name of this Kata). Strings passed in will consist of only 
letters and spaces. Spaces will be included only when more than one word is present.
'''

def spin_words(sentence):
    return ' '.join([ word[::-1] if len(word) > 4 else word for word in sentence.split()])

print(spin_words("Hey fellow warriors"))