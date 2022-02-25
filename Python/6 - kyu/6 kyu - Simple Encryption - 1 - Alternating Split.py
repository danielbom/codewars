# https://www.codewars.com/kata/simple-encryption-number-1-alternating-split/train/python
# My solution
import itertools

def decrypt(encrypted_text, n):
    if not encrypted_text or not n:
        return encrypted_text
    length = len(encrypted_text) // 2
    for _ in range(n):
        p1 = encrypted_text[:length]
        p2 = encrypted_text[length:]
        encrypted_text = ''.join(i + j for i,j in itertools.zip_longest(p2, p1, fillvalue=''))
    return encrypted_text

def encrypt(text, n):
    for _ in range(n):
        text = text[1::2] + text[::2]
    return text

# Other ways
def decrypt(text, n):
    if text == None: return text

    decodeList = encrypt(list(range(len(text))),n)
    return ''.join( text[decodeList.index(i)] for i in range(len(text)) )


def encrypt(text, n):
    if text == None: return text
    return encrypt(text[1::2] + text[0::2],n-1) if n>0 else text
