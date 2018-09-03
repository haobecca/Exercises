'''
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
'''

def find_short(sentence):
    return min([len(word) for word in sentence.split()])



sentence = 'bitcoin take over the world maybe who knows perhaps'    
print(find_short(sentence))