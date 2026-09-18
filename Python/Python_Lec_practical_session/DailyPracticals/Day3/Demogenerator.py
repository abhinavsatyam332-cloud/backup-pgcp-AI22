def get_num():
    i = 0
    while True:
        yield i
        i+=1
series = get_num()

print(next(series))
print(next(series))
print(next(series))




print("\n\n")
def get_fib(end):
    i = 0
    a,b = 0,1
    while i<end:
        yield b
        a,b = b,a+b
        i+=1

fibseries = get_fib(20)
print(next(fibseries))
print(next(fibseries))
print(next(fibseries))
print(next(fibseries))
print(next(fibseries))
print(next(fibseries))