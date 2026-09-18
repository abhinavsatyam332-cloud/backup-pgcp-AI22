from functools import reduce

numbers = [i for i in range(20,30)]

evens = list(filter(lambda n: n%2==0 , numbers))

total = reduce(lambda n1,n2: n1+n2, numbers)
print(total)

words = ["df","fg","hfdg"]
s_upper = list(map(lambda s:s.upper() , words))
print(s_upper)

statting_with_h = list(filter(lambda s: s.startswith('h') , words))
print(statting_with_h)

print(evens)