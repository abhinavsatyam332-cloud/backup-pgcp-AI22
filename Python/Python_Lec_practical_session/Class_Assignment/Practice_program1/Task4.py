'''

Q.4.  Write a Python function that takes a list of words and returns the length of the longest one

'''

def fun(words):
    lengths = [len(word) for word in words]
    return max(lengths)

user_ip = input("Enter words space separated: ")
user_ip = user_ip.split(" ")
print("Max length of word is: ",fun(user_ip))