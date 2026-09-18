# Q.1 In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is replaced by a
# letter some fixed number of positions down the alphabet.
# For example, with a shift of 3, A would be replaced by D, B would become E, and so on. Create a cipher to represent each key with corresponding value as :
#
# {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o',
#   'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}
#
# Expected output : decrypted = python



'''
s= {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o',
  'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}

dic= {v:k for k,v in s.items()}
a=[]
encrypted = 'sbwkrq'
for e in encrypted:
    a.append(dic[e])

print("".join(a))

'''
from pprint import pprint

# Q.2 For a given dictionary
#
# emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
#             'Aditi': ['Python', 'PHP', 'Database']}
#
# 1. Print employees and their skill sets
# 2. Find all the employees who know Java
# 3. Update skill for an employee
# 4. Add/remove employee data


emp_data = {'Amol': ['C', 'C++', 'Java'],
            'Aditya': ['Angular', 'Java'],
            'Aditi': ['Python', 'PHP', 'Database']}

# pprint(emp_data)

emp=emp_data
for emp in emp_data:
    if "Java" in emp_data[emp]:
        print(emp)
#3
emp_data['Amol'].append("Python")
print(emp_data['Amol'])

#4

emp_data["Satyam"]=['Python', 'PHP', 'Database']
pprint(emp_data)
pprint("------------------------")
emp_data.pop("Aditi")
pprint(emp_data)