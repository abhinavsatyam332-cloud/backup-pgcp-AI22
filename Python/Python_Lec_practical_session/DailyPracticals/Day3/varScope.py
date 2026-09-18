import builtins

len = 3

name = 'Abhi'
age =19
#
# print(name)
# print(builtins.len(name))
def display_details():
    name = 'ram'
    age = 90
    print(f'{name} = {age}')

if __name__ == '__main__':
    print(f'{name} = {age}')
    display_details()

# display_details()