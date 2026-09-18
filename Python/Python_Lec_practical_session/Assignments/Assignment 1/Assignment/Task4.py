num = 23456
b=num
digit=0
sum1=0
even=0
odd=0
a=0
while num !=0 :
   digit+=1
   a=num%10
   sum1 = sum1 +a
   if(a%2 == 0):
       even+=1

   else:
       odd+=1


   num=num//10
print(f"The number: {b}")
print(f"Output digits: {digit}")
print(f"Sum of digits: {sum1}")
print(f"Even: {even}")
print(f"Odd: {odd}")
