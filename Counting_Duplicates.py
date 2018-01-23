'''
kata : https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
'''

def duplicate_count(text):
    text = text.lower()
    s = set()
    for c in text:
        if text.count(c) > 1:
            s.add(c)
            
    return len(s)