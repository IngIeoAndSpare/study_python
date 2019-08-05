'''
kata : https://www.codewars.com/kata/54da5a58ea159efa38000836
'''

def find_it(seq):
    cut_arr = seq[:]
    for item in seq:
        if (seq.count(item) % 2) == 0:
            cut_arr.remove(item)
    
    return cut_arr[0]