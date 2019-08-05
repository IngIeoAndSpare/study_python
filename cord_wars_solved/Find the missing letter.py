'''
kata : https://www.codewars.com/kata/5839edaa6754d6fec10000a2
'''
def find_missing_letter(chars):
    asc = [ord(c) for c in chars]
    offset = asc[0]
    for item in asc:
        if item != offset:
            return chr(item - 1)
        offset = offset + 1