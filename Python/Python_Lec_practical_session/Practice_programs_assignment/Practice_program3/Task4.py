'''

Q. 4. Create series of 'n' prime numbers and display first 10
'''

import  math

def printNrimes(n):
    i = 1
    nCounter = 1
    isPrime = True
    while(True):


        for j in range(2,  int(math.sqrt(i)+1)):
            if(i % j == 0 and i!=j):
                isPrime = False
                break

        if isPrime==True:
            nCounter += 1
            print(i)

        isPrime = True
        i += 1

        if nCounter == n+1:
            break

n = int(input("Enter n: "))
print(f"\nfirst {n} Prime Numbers")
printNrimes(n)






