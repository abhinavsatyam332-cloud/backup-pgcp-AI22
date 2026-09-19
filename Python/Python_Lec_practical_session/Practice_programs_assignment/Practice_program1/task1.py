'''

Q.1A. Write a program that asks the user how many days are in a particular month, and
what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then
prints a calendar for that month. For example, here is the output for a 30-day month that begins on day 3 (Thursday):
M  T  W  T  F  S  S
      	 1  2  3  4
5  6  7  8  9 10 11

'''


daysInMonth = int(input("Enter how many days in a month"))
monthBeginsOn = int(input("Day of the week the month begins: "))

print("M  T  W  T  F  S  S")

for i in range(1,daysInMonth+1):
    if(i==1):
        print("   "* (monthBeginsOn),end="")

    if(i>0 and i<10):
        print(i,end="  ")
    else:
        print(i,end=" ")

    if((i+ monthBeginsOn) % 7 ==0):
        print("")


