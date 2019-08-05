'''
kata : https://www.codewars.com/kata/565f448e6e0190b0a40000cc
'''

def actually_really_good(foods):
    sentence = "You know what's actually really good? "
    if not foods:
        return sentence + "Nothing!"
    
    return  sentence + '{} and {}.'.format(foods[0].capitalize(), foods[1].lower() if len(foods) > 1 else 'more {}'.format(foods[0].lower()))
    