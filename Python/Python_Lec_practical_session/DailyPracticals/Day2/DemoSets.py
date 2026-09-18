colors1 = {'red', 'yellow', 'orange', 'blue', 'purple'}
colors1.clear()

colors1 = {'red', 'yellow', 'orange', 'blue', 'purple'}
colors2 = ['blue', 'purple']

# colors2.add('blue')
# colors2.discard('blue')
# print(colors1.pop())

print(colors1.union(colors2))
# print(set(colors1 & colors2))
print(colors1.intersection(colors2))

print(colors1 - set(colors2))
colors1.update([1, 2])
print(colors1.symmetric_difference(colors2))

dict1 = {'k1': 1,
         'k2': 2
         }
dict1.keys()
dict1.values()
dict1.items()




for key, value in dict1.items():
    print(f'{key} values {value}')

list1 = [
    {
        'a': 34
    },
    {
        'b': 21
    }
]

for key, value in list1[0].items():
    print(f'{key} : {value}')
