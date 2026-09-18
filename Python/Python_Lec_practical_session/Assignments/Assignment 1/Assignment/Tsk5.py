num1 = 3
num2=5
a=num2
b=num1
while b!=0:

   remin=a%b
   a=b
   b=remin

print(f"HCF: {a}")
lcm=(num1*num2)//a
print(f"LCM: {lcm}")