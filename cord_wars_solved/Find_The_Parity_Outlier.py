'''
kata : https://www.codewars.com/kata/5526fc09a1bbd946250002dc

'''

def find_outlier(integers):
    odd = []
    even = []
    
    for item in integers:
        (even if item % 2 == 0 else odd).append(item)
    poo = odd[0] if len(odd) < 2 else even[0]
    return poo