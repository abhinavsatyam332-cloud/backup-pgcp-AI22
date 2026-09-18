num = 321
mul=100
i=0
while num/10!=0 :
    i=i+mul*(num%10)
    mul=int(mul/10)
    num=int(num/10)
print(i)

