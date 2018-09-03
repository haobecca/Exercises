'''
Bob answers 'Sure.' if you ask him a question.
He answers 'Whoa, chill out!' if you yell at him.
He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else.
'''
'''
This solution will avoid checking if phrase is a question twice, but if phrase is yelling will still be checked twice

def hey(phrase):
    phrase = phrase.strip()
    #check if no characters
    if phrase == '':
        return 'Fine. Be that way!'
    #check if question
    elif phrase[-1] == '?':
        #check if all caps AND question
        if phrase.isupper():
            return 'Calm down, I know what I\'m doing!'
        else:
            return 'Sure.'    
    #check if all caps
    elif phrase.isupper():
        return 'Whoa, chill out!'
    #else return 'Whatever'
    else:
        return 'Whatever.'
'''
# This solution allows each condition to only be checked once by using a flag system, so no order dependency. However, another set of conditionals around the flags will have to be checked.
def hey(phrase):
    phrase = phrase.strip()
    #check if no characters
    if phrase == '':
        return 'Fine. Be that way!'
    #check if question
    flag = ''
    if phrase[-1] == '?':
        flag = flag + 'question'
    if phrase.isupper():
        flag = flag +'yell'  
    if flag == 'question':
        return 'Sure.'
    elif flag == 'yell':
        return 'Whoa, chill out!'
    elif flag == 'questionyell':
        return 'Calm down, I know what I\'m doing!'
    else:
        return 'Whatever.'

'''
test_cases = ["Okay if like my  spacebar  quite a bit?   ","WATCH OUT!", "Does this cryogenic chamber make me look fat?", "Let's go make out behind the gym!", "WHAT THE HELL WERE YOU THINKING?", "1, 2, 3", "1, 2, 3 GO!", "ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!", "\t\t\t\t\t\t\t\t\t\t"]

for case in test_cases:
    print(hey(case))

''' 
