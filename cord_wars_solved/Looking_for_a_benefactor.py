'''
kata : https://www.codewars.com/kata/569b5cec755dd3534d00000f
'''

import math
def new_avg(arr, newavg):

    answer = newavg * (len(arr) + 1) - sum(arr)
    if answer < 0:
        raise ValueError()
    
    return math.ceil(answer)