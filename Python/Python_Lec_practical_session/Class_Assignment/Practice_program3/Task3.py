'''
Q.3. Function display_greeting(message) prints message sent as argument as today's greeting.
 Decorate the function using appropriate decorated so that the greeting is displayed using Uppercase.
'''
def to_uppercase(inner):
    def wrapper(*args, **kwargs):
        word, = args
        print(word)
        word = word.upper()
        return inner(word)
    return wrapper
@to_uppercase
def greeting(message):
    print(message)

greeting("hello!!")