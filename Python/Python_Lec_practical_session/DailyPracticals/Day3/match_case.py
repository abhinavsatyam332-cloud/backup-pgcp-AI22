from random import choice

import Math
from Math import add,substract,multiply,divide
from Math import multiply as mlt

num1 = int(input('Enter first num: '))
num2 = int(input('Enter second num: '))

choice = int(input('Enter your choice \n 1.add  \n 2.substract  \n 3.Multiply   \n 4.Divide \n'))

match choice:
    case 1:
        print(add(num1,num2))
    case 2:
        print(substract(num1,num2))
    case 3:
        print(mlt(num1,num2))
    case 4:
        print(divide(num1,num2))
