'''
kata : https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
'''

def accum(s):
    arr = list(s.upper())
    result = ''
    i = 0
    for item in arr:
        result += item + (item * i).lower() + '-'
        i += 1
    return result[:-1]