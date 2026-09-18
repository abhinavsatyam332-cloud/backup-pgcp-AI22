
import  time
from time import sleep


def keep_time(inner):
    def wrapper():
        start =  time.time()

        inner()
        end = time.time()
        print(f"Time taken: {end - start}")
    return wrapper


@keep_time
def print_squares():
    for  i in range(10):
        print(i*i )

print(print_squares())











print("\n\n\n")

def smart_math(inner):
    def wrapper(*args, **kwargs):
        a,b = args        # unpacking
        if a<b:
            a,b=b,a
        return inner(a,b)   
    return wrapper

@smart_math
def substract(n1,n2):
    return n1- n2

print(substract(2,10))
print(substract(10,2))


# print_squares()

# keep_time(print_squares)