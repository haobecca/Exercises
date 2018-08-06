"""
Take a list of ages when each of your great-grandparent died.
Multiply each number by itself.
Add them all together.
Take the square root of the result.
Divide by two.
Example

predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
Note: the result should be rounded down to the nearest integer.

Some random tests might fail due to a bug in the JavaScript implementation. Simply resubmit if that happens to you.
"""
import decimal
ages = [65, 60, 75, 55, 60, 63, 64, 45]
def predict_age(*ages):
    return int(( sum([age*age for age in ages]) ** 0.5) / 2)




print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))
