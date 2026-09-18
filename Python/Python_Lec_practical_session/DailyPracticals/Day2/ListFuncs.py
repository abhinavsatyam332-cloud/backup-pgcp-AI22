
lst = ["you","this", "is","list","hello","how","are","you"]

for item in lst:
    print(item.upper())

print(lst[0])
print(lst[-1:-4:-1])
print(lst[0:2]+lst[6:])

lst.append(0)
lst.insert(2,"insrt")

print(lst)
print(lst.pop(2))
print(lst)
print(lst.index("you"))

# lst.append([1,2,3])
lst.extend((1,2,3))

print(lst.index("you"))
print(lst.index("you", 3 ,len(lst)))

a, b, c, d, e, f, g, h, *extra, j = lst

print(c)  # This will print: is
print(j)  # This will print the very last element (0)
print(c)





# print(lst)
from math import sqrt

sqrt(10)
my_list=[[1,"one"],[2,"two"]]

for item in my_list:
    print(item)








# List comprehension

numbers = [i for i in range(10)]
squares  = [num*num for num in numbers]
print(squares)
squares  = [num*num for num in numbers if num %2==0]
print(squares)

evenOdd = ['even' if num %2 ==0 else 'odd' for num in numbers]
print(evenOdd)


my_list=[[1,"one"],[2,"two"],[3,"three"],[4,"four"]]

print_len = [len(val) for ind,val in my_list] # dictionary comprehension
print_len2=[len(item[1]) for item in my_list]
print( print_len)
print(print_len2)

sent = "was it the rat , i saw?"
vowels = [ch for ch in sent if ch in ['a','e','i','o','u']]
print(vowels)

list1 = [1,2,3,5]
list1.append([90,43])
list1.extend(([54,88]))
name="kla7a"
print(name.isalpha())
print(list1)


clean_sent = "".join([char for char in sent if char.isalnum()])
print(clean_sent)
print('abc 2 3'.isalnum())

t1 = (1, 3, 4)
t2 = ('a', 2, 5.5)
t3 = (3, "my name")

list1 = list(t3)
list1.append(3333)

for a, b, c in t1, t2, list1:
    print(f'{a},{b},{c}')

t1 = [1,2,3]
t2 = [10,20,30]
t3 = [100,200,300]
n1,n2,n3 = t1
print(n1)


zipped = list(zip(t1,t2,t3))
print(zipped)
a1,a2,a3 = zip(*zipped)
print(a1)