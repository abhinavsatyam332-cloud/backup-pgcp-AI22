'''
Q.2 For a given dictionary

emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
            'Aditi': ['Python', 'PHP', 'Database']}

1. Print employees and their skill sets
2. Find all the employees who know Java
3. Update skill for an employee
4. Add/remove employee data

'''

emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
            'Aditi': ['Python', 'PHP', 'Database']}

def getEmpInfo():
    for k , v in emp_data.items():
        s = ''
        for item in v:
            s += f" {item},"
        print(f"Name -> {k}\nSkills -> {s}")
        print("."*5)

getEmpInfo()

res = [k for k,v in emp_data.items() if 'Java' in v]
print(res)

def addSkill(name, skill):
    emp_data.get(name).append(skill)
    print(emp_data[name])

addSkill("Amol", "Python")

def removeEmployee(name):
    em = emp_data.pop(name)
    print(f"{name} removed from employee list")

removeEmployee("Amol")
print(emp_data)