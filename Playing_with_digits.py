'''
kata : https://www.codewars.com/kata/5552101f47fc5178b1000050
'''
def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += pow(int(i), p)
        p += 1
    return int(sum / n) if sum % n == 0 else -1