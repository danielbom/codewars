# https://www.codewars.com/kata/consecutive-strings/train/python
# My solution
def longest_consec(list_words, k):
    if ( k <= 0 or k > len( list_words ) ): # Avoiding invalid inputs
        return ""
    
    str_longest = ''
    len_longest = 0
    
    for i in range( len(list_words) - k + 1 ):
        new_str_longest = ''.join(list_words[i:k+i])
        new_len_longest = len( new_str_longest )
        
        if ( new_len_longest > len_longest ):
            str_longest = new_str_longest
            len_longest = new_len_longest
        
    return str_longest

# ...
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result
# ...
def longest_consec(strarr, k):
    if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr))]
    return max(lst, key= lambda x: len(x))
# ...
def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ''
    return max(
        (''.join(strarr[i:i + k]) for i in range(len(strarr) - k + 1)), 
        key=len
    )
