'''


Q.1 In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is replaced by a letter
some fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on.
 Create a cipher to represent each key with corresponding value as :

{'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}

encrypted = 'sbwkrq'
Expected output : decrypted = python


'''

# print(ord('A'))
# print(chr(65))

encrypted = 'sbwkrq'
decrypted = ''



def decrept(code):
    dic = {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n',
           'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y',
           'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}
    rev_dict = {v: k for k, v in dic.items()}
    res = ''
    for ch in code:
        res += rev_dict[ch]
    return res
print(decrept('sbwkrq'))