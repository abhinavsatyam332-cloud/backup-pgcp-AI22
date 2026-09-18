# name = input()
# print(name)
# hello = input("HEllo my name is: ")
# print(hello)
#
# # concat
#
# print(name , hello)
#
# age = 5;
# print(f"name is {name}")
# print("name is {} and age is {}".format(name,age))
# print(f'you entered name{name}')



data1 = 4e6  # can also write 4e - 6
print(f"{data1:.2f}")
print(f"{data1:.0f}")

data1 = 4e-6
print(f"{data1:.7f}")
print(f"{data1:.7f}")

data2 = 0.65
print(f"{data2:.0%}")

name = "abc"
print(f"left end {name:^10} right end")
print(f"left end {name:>10} right end")
print(f"left end {name:<10} right end")

dollar = 10000
print(f"₹{dollar:,.2f}")

import keyword

