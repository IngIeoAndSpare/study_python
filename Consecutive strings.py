'''
kata :https://www.codewars.com/kata/56a5d994ac971f1ac500003e
'''
def longest_consec(strarr, k):
    
    st_len = len(strarr)
    if (st_len < k or k < 1 or st_len == 0):
        return ""
    
    length_arr = [
      sum(len(word) for word in strarr[i:i+k])
      for i in range(len(strarr) - k + 1)
      ]
    
    max_point = max(enumerate(length_arr), key=lambda x: x[1])[0]
    
    return ''.join(strarr[max_point:max_point+k])