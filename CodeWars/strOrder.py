'''
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.
For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"

def order(sentence):
    order = [int(num) for num in sentence if num in     '0123456789']
    words = sentence.split()
    order_dict = dict(zip(order, words))
    sen_len = list(range(1, len(words) + 1))
    new = [order_dict[n] for n in sen_len]
    return ' '.join(new)
'''

def order(sentence):
    def number(word):
        return next(int(num) for num in word if num.isdigit())
    return ' '.join(sorted(sentence.split(), key = number))

