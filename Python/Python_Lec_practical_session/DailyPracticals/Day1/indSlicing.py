
str = "this is fiRSt string"

print(str[0])
print(str[0:5])
print(str[2:3])
print(str[-1])
print(str[-5:-2])
print(str[-2:-7:-1])
print(str[::-1])
print(str[0:10:3])

print(str.isalpha())
str.isdecimal()
str.isdigit()
str.isnumeric()

# str = "345"
print(str.isalnum())

print(str.upper())
print(str.lower())

lst = str.split(' ')

print(lst)
s2 = ' '.join(lst)
print(s2)

strrr = "345"
a = 1
print(strrr.find('3'))
strrr.rfind('3')
strrr.index('5')

strrr.strip()
strrr.rstrip()


str = "thi fiRSt string"
parts = str.partition(' ')
print(parts)