'''
The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("
"recede" => "()()()"
"Success" => ")())())"
"(( @" => "))(("
'''

'''
def duplicate_encode(word):
    word = word.lower()
    word_key = [character for character in word]
    word_value = [word.count(character) for character in word]
    word_dict = dict(zip(word_key, word_value))
    new_string = ['(' if word_dict[character] == 1 else ')' for character in word]
    return ''.join(new_string)
'''

def duplicate_encode(word):
    word = word.lower()
    new_string = ['(' if word.count(character) == 1 else ')' for character in word]
    return ''.join(new_string)


test_cases = ['din', 'recede', 'Success', '(( @', 'mQucIz)@!b(ddm(m(z']

for case in test_cases:
    print(duplicate_encode(case))