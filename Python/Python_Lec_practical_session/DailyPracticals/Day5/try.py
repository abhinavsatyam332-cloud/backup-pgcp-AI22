import sys

try:
    divident = int(input('Enter a divident: '))
    divisor = int(input('Enter a divisor: '))
    res = divident / divisor
    raise ZeroDivisionError("dfg")
    print(res)


except ValueError as er:
    print(er)

except ZeroDivisionError as er:
    print(er)
    type, cause, traceback = sys.exc_info()
    print(f'{type}, {cause}, {traceback}')
    

else:
    print("If try is succed this executed")
finally:
    print("Always executed")


for i in range(10):
    print(i)
    if i==2:
        break

else:
    print("else exec")