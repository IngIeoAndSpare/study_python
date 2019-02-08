import numpy as np
import pickle
import os

if __name__ == "__main__":
    data1 = {'a' : [1,2,3,4], 'b' : 10000, 'c': None}
    output = open('data.pkl', 'wb')
    pickle.dump(data1, output)
    output.close()
    pkifile = open('data.pkl', 'rb')
    data2 = pickle.load(pkifile)

    print(data2)