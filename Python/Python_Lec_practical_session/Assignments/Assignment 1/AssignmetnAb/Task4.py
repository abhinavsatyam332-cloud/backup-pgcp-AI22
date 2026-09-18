num = 23456

no = num
r = 0
rev = 0
digitCounter =0
digitSum = 0
evenC = 0
oddC = 0

while no!=0:
    r = no % 10
    digitCounter += 1
    digitSum +=r
    if r % 2 == 0:
        evenC+=1
    else:
        oddC+=1


    no = no //10

print(f"Output digits: {digitCounter}")
print(f"Sum: {digitSum}")
print(f"Even Digits: {evenC}")
print(f"Odd Digits: {oddC}")

