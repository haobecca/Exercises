"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

For example:
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""

def sleep_in(vaycay):
    if vaycay in ['yes', 'Yes', 'YES']:
        return True
    else:
        day = input('What day is it in the week? ')
        if day.lower() in ['saturday', 'sunday']:
            return True
        else:
            print('We are not sleeping in')
            return False


vaycay = input('Are we on vacation? ')

if sleep_in(vaycay):
    print('We are sleeping in')

