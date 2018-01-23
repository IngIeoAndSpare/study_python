'''
kata : https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c
'''

def sort_by_length(arr):
    poo = []
    sorting = []
    result = []
    
    for item in arr:
        poo.append(len(item))
        sorting.append(len(item))
        
    sorting.sort()
    
    for item in sorting:
        result.append(arr[poo.index(item)])
    
    return result