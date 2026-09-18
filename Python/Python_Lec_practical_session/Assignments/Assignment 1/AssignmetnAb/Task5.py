num1 = 3
num2 = 6
hcf = 1
for i in range(1,max(num1,num2)):
    if(num1 % i == 0 and num2 %i==0):
        hcf = i

print("HCF: ",hcf)
print("LCM: ",(num1*num2)//hcf)