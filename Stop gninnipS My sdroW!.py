'''
kata : https://www.codewars.com/kata/5264d2b162488dc400000001
'''
def spin_words(sentence):
    test = sentence.split()
    if(len(test) == 1):
        if(len(test[0]) > 4):
            return test[0][::-1]
        return test[0]
        
    temp = []
    for item in test :
        temp.append(item[::-1]) if len(item) > 4 else temp.append(item)
    return ''.join(str(x)+' ' for x in temp)[:-1]
