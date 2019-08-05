def spin_words(sentence, sentence2):
    
    test1 = sentence.split()
    test2 = sentence2.split()

    temp = list(set(test1) - set(test2))
    result = []
    for item in temp:
        result.insert(test1.index(item), item)

    return filter(None, result)